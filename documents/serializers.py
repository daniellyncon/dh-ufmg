from djoser.serializers import UserSerializer

from axis.serializers import AxisSerializer
from cases.related_serializer import RelatedCaseSerializer
from people.related_serializer import RelatedPersonSerializer
from tasks.related_serializer import RelatedTaskSerializer
from .models import Document
from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):

    prepared_by = UserSerializer(many=True, read_only=False, required=False)
    axis = AxisSerializer(many=True, read_only=False, required=False)
    tasks = RelatedTaskSerializer(many=True, read_only=False, required=False)
    person_document = RelatedPersonSerializer(many=True, read_only=False, required=False)
    case_documents = RelatedCaseSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Document
        fields = ('id', 'type', 'recipients', 'date', 'link', 'prepared_by', 'axis', 'tasks', 'person_document',
                  'case_documents')
