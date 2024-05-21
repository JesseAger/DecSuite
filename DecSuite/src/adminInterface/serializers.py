# adminInterface/serializers.py
from rest_framework import serializers
from .models import FirewallRule

class FirewallRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirewallRule
        fields = ['id', 'rule_type', 'ip_address', 'description', 'created_at']
