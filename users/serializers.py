from rest_framework.serializers import ModelSerializer
from users.models import User, OnDuty


class OnDutySerializer(ModelSerializer):
    class Meta:
        model = OnDuty
        fields = '__all__'


class UserSerializer(ModelSerializer):
    on_duty = OnDutySerializer(many=True)
    class Meta:
        model = User
        fields = ('name', 'email', 'bond_type', 'phone', 'registration', 'street_address', 'number_address', 'complement_address', 
            'neighborhood_address', 'city_address', 'state_address', 'course', 'university', 'department', 'rg', 'cpf', 'cnh', 
            'date_joined', 'date_fired', 'is_active', 'scholarship', 'scholarship_type', 'on_duty'
        )
