# from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from address.serializers import AddressSerializer
from .models import User


class UserSerializer(WritableNestedModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ('name', 'email', 'bond_type', 'phone', 'registration', 'address',
                  'course', 'university', 'department', 'rg', 'cpf', 'cnh',
                  'date_joined', 'date_fired', 'is_active', 'scholarship', 'scholarship_type')
