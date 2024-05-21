from django.db import models

# Create your models here.
# logApp/models.py

class DetailedLog(models.Model):
    ip_address = models.GenericIPAddressField()
    request_method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    request_headers = models.TextField()
    response_status = models.IntegerField()
    response_headers = models.TextField()
    response_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
