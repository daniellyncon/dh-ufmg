from rest_framework import serializers
from users.models import User


class RelatedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'bond_type', 'phone', 'registration', 'course', 'university', 'department',
                  'rg', 'cpf', 'cnh', 'date_joined', 'date_fired', 'is_active', 'scholarship', 'scholarship_type')
