from rest_framework.viewsets import ModelViewSet
from .models import JudicialAppeal
from .serializers import JudicialAppealSerializer

# Create your views here.

class JudicialAppealViewSet(ModelViewSet):
    queryset = JudicialAppeal.objects.all()
    serializer_class = JudicialAppealSerializer