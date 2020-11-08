from .models import JudicialAppeal, JudicialAppealMove
from rest_framework import serializers


class JudicialAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudicialAppeal
        fields = '__all__'


class JudicialAppealMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudicialAppealMove
        fields = '__all__'
