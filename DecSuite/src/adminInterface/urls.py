# adminInterface/urls.py
from django.urls import path
from .views import FirewallRuleListCreateAPIView, FirewallRuleRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('firewall-rules/', FirewallRuleListCreateAPIView.as_view(), name='firewall-rule-list-create'),
    path('firewall-rules/<int:pk>/', FirewallRuleRetrieveUpdateDestroyAPIView.as_view(), name='firewall-rule-detail'),
]
