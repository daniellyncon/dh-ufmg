from rest_framework.viewsets import ModelViewSet
from .models import LawSuit
from .serializers import LawSuitSerializer

# Create your views here.

class LawSuitViewSet(ModelViewSet):
    queryset = LawSuit.objects.all()
    serializer_class = LawSuitSerializer