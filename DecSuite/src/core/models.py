from django.db import models

# Create your models here.

class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    request_method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_malicious = models.BooleanField(default=False)

class Threat(models.Model):
    request = models.ForeignKey(RequestLog, on_delete=models.CASCADE)
    threat_type = models.CharField(max_length=50)
    detected_at = models.DateTimeField(auto_now_add=True)
