from rest_framework import serializers
from axis.serializers import AxisSerializer
from cases.related_serializer import RelatedCaseSerializer
from people.related_serializer import RelatedPersonSerializer
from address.serializers import AddressSerializer
from .models import Entity


class EntitySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, read_only=False, required=False)
    person = RelatedPersonSerializer(many=True, read_only=False, required=False)
    case_entities = RelatedCaseSerializer(many=True, read_only=False, required=False)
    axis = AxisSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Entity
        fields = ('id', 'name', 'entity_liked', 'description', 'contact', 'reference_person',
                  'reference_person_contact', 'comments', 'address', 'person', 'axis', 'case_entities')
