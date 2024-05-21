from django.shortcuts import render

# Create your views here.
# logApp/views.py
from rest_framework import viewsets
from .models import DetailedLog
from .serializers import DetailedLogSerializer

class DetailedLogViewSet(viewsets.ModelViewSet):
    queryset = DetailedLog.objects.all()
    serializer_class = DetailedLogSerializer
