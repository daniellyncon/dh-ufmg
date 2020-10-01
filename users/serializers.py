from people import serializers
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('name', 'email', 'bond_type', 'phone', 'registration', 'street_address', 'number_address', 'complement_address', 
            'neighborhood_address', 'city_address', 'state_address', 'course', 'university', 'department', 'rg', 'cpf', 'cnh', 
            'date_joined', 'date_fired', 'is_active', 'scholarship', 'scholarship_type')
    
