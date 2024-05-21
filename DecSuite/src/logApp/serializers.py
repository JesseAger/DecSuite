# logApp/serializers.py

from rest_framework import serializers
from .models import DetailedLog

class DetailedLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedLog
        fields = '__all__'
