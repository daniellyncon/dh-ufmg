from drf_writable_nested.serializers import WritableNestedModelSerializer
from address.serializers import AddressSerializer
from on_duty.serializers import OnDutySerializer
from .models import User


class UserSerializer(WritableNestedModelSerializer):
    address = AddressSerializer()
    on_duty = OnDutySerializer(required=False, allow_null=True, many=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'bond_type', 'phone', 'registration', 'address',
                  'course', 'university', 'department', 'rg', 'cpf', 'cnh', 'on_duty',
                  'date_joined', 'date_fired', 'is_active', 'scholarship', 'scholarship_type')
