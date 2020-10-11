import datetime

from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Person
from address.serializers import AddressSerializer


class PersonSerializer(WritableNestedModelSerializer):
    address = AddressSerializer()
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    @staticmethod
    def get_age(instance):
        today = datetime.date.today()
        return today.year - instance.birthday.year - ((today.month, today.day) <
                                                      (instance.birthday.month, instance.birthday.day))

