from .models import Case
from rest_framework import serializers


class CaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Case
        fields = '__all__'