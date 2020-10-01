from rest_framework.viewsets import ModelViewSet
from .models import OnDuty
from .serializers import OnDutySerializer


class OnDutyViewSet(ModelViewSet):
    queryset = OnDuty.objects.all()
    serializer_class = OnDutySerializer
