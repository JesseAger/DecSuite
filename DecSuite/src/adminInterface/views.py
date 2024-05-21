from django.shortcuts import render

# Create your views here.
# adminInterface/views.py
from rest_framework import generics
from .models import FirewallRule
from .serializers import FirewallRuleSerializer

class FirewallRuleListCreateAPIView(generics.ListCreateAPIView):
    queryset = FirewallRule.objects.all()
    serializer_class = FirewallRuleSerializer

class FirewallRuleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirewallRule.objects.all()
    serializer_class = FirewallRuleSerializer
