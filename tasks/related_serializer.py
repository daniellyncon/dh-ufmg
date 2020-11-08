from rest_framework import serializers
from .models import Task


class RelatedTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'deadline', 'description', 'workflow_state')
        read_only_fields = ('workflow_state',)
