from rest_framework.viewsets import ModelViewSet
from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filterset_fields = ('type', 'date', 'prepared_by', 'axis', 'tasks')
