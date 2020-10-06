from rest_framework import viewsets
from .models import Axis
from .serializers import AxisSerializer


class AxisViewSet(viewsets.ModelViewSet):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer