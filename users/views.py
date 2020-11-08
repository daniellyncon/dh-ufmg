from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('axis', 'bond_type', 'course', )
