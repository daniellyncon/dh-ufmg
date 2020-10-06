from rest_framework import serializers
from .models import Axis


class AxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axis
        fields = '__all__'
