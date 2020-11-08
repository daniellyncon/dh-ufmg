from rest_framework.viewsets import ModelViewSet
from .models import JudicialAppeal, JudicialAppealMove
from .serializers import JudicialAppealSerializer, JudicialAppealMoveSerializer


class JudicialAppealViewSet(ModelViewSet):
    queryset = JudicialAppeal.objects.all()
    serializer_class = JudicialAppealSerializer
    filterset_field = ('type', 'plenary', 'law_suit', )


class JudicialAppealMoveViewSet(ModelViewSet):
    queryset = JudicialAppealMove.objects.all()
    serializer_class = JudicialAppealMoveSerializer
    filterset_field = ('judicial_appeal', 'date', )
