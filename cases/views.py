from rest_framework.viewsets import ModelViewSet
from .models import Case
from .serializers import CaseSerializer


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    filterset_fields = ('intern', 'assisted_person', 'law_suits', 'entities', 'axis', 'tasks', 'documents')
