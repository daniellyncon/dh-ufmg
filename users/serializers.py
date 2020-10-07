from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('name', 'email', 'bond_type', 'phone', 'registration',
                  'course', 'university', 'department', 'rg', 'cpf', 'cnh',
                  'date_joined', 'date_fired', 'is_active', 'scholarship', 'scholarship_type')

