from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Person
from address.serializers import AddressSerializer


class PersonSerializer(WritableNestedModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Person
        fields = '__all__'
