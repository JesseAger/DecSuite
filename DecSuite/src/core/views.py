from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# core/views.py

from rest_framework import viewsets
from .models import RequestLog, Threat
from .serializers import RequestLogSerializer, ThreatSerializer

class RequestLogViewSet(viewsets.ModelViewSet):
    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer

class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer
def Intro(request, *args, **kwargs):
    return HttpResponse('<h2>DecSuite</h2>')
