# core/middleware.py

from django.http import HttpResponse
from core.models import RequestLog
from logApp.models import DetailedLog

class RequestInspectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        ip_address = request.META.get('REMOTE_ADDR')
        path = request.path
        request_method = request.method
        request_headers = dict(request.headers)

        # Log the request
        log = RequestLog.objects.create(ip_address=ip_address, request_method=request_method, path=path)

        # Placeholder for AI model analysis
        # is_malicious = analyze_request(ip_address, path, request_method)
        is_malicious = False  # Replace with actual analysis result

        log.is_malicious = is_malicious
        log.save()

        if is_malicious:
            # Log detailed information
            DetailedLog.objects.create(
                ip_address=ip_address,
                request_method=request_method,
                path=path,
                request_headers=request_headers,
                response_status=403,
                response_headers={'Content-Type': 'text/plain'},
                response_body='Blocked by DecSuite',
            )
            return HttpResponse('Blocked by DecSuite', status=403)

        # Get the response
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
        )

        return response
