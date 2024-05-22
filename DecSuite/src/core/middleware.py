from django.http import HttpResponse
from core.models import RequestLog
from logApp.models import DetailedLog
from adminInterface.models import FirewallRule
from core.utils import retaliate
from core.ai_model import analyze_request  # Importing AI model function
import os
import subprocess

class RequestInspectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        path = request.path
        request_method = request.method
        request_headers = dict(request.headers)

        # Log the request
        log = RequestLog.objects.create(ip_address=ip_address, request_method=request_method, path=path)

        # Analyze the request using AI model
        is_malicious, attack_type = analyze_request(ip_address, path, request_method, request_headers)
        
        if is_malicious:
            log.is_malicious = True
            log.save()

            # Block the request
            DetailedLog.objects.create(
                ip_address=ip_address,
                request_method=request_method,
                path=path,
                request_headers=request_headers,
                response_status=403,
                response_headers={'Content-Type': 'text/plain'},
                response_body='Blocked by DecSuite Firewall',
                is_malicious=True  # Mark as malicious
            )

            # Execute the corresponding retaliation script
            script_name = f"{attack_type.lower()}.py"
            script_path = os.path.join("core", "scripts", script_name)
            if os.path.exists(script_path):
                subprocess.run(["python", script_path, ip_address])
            else:
                print(f"Retaliation script for {attack_type} not found: {script_path}")

            return HttpResponse('Blocked by DecSuite Firewall', status=403)

        # If not malicious, proceed normally
        response = self.get_response(request)

        # Log detailed information
        DetailedLog.objects.create(
            ip_address=ip_address,
            request_method=request_method,
            path=path,
            request_headers=request_headers,
            response_status=response.status_code,
            response_headers=dict(response.items()),
            response_body=response.content.decode(),
            is_malicious=False  # Mark as not malicious
        )

        return response
