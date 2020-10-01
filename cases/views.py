from rest_framework.viewsets import ModelViewSet
from .models import Case
from .serializers import CaseSerializer


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer