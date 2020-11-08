from rest_framework.viewsets import ModelViewSet
from .models import LawSuit
from .serializers import LawSuitSerializer


class LawSuitViewSet(ModelViewSet):
    queryset = LawSuit.objects.all()
    serializer_class = LawSuitSerializer
    filterset_fields = ('law_area', 'has_lawyer', 'lawyer_name', 'followed_by_daj', )
