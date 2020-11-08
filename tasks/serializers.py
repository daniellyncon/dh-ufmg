from djoser.serializers import UserSerializer
from drf_writable_nested import WritableNestedModelSerializer
from cases.related_serializer import RelatedCaseSerializer
from documents.related_serializer import RelatedDocumentSerializer
from .models import Task


class TaskSerializer(WritableNestedModelSerializer):
    responsible = UserSerializer(many=True, read_only=False, required=False)
    case_tasks = RelatedCaseSerializer(many=True, read_only=False, required=False)
    document_task = RelatedDocumentSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Task
        fields = ('id', 'title', 'deadline', 'description', 'workflow_state', 'responsible', 'case_tasks',
                  'document_task')
        read_only_fields = ('workflow_state', )
