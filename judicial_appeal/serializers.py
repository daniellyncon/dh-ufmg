from .models import JudicialAppeal
from rest_framework import serializers


class JudicialAppealSerializer(serializers.ModelSerializer):

    class Meta:
        model = JudicialAppeal
        fields = '__all__'