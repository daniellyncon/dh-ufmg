from rest_framework.viewsets import ModelViewSet
from .models import JudicialAppeal, JudicialAppealMove
from .serializers import JudicialAppealSerializer, JudicialAppealMoveSerializer

# Create your views here.

class JudicialAppealViewSet(ModelViewSet):
    queryset = JudicialAppeal.objects.all()
    serializer_class = JudicialAppealSerializer

class JudicialAppealMoveViewSet(ModelViewSet):
    queryset = JudicialAppealMove.objects.all()
    serializer_class = JudicialAppealMoveSerializer