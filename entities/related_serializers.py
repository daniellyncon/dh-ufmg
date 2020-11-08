from rest_framework import serializers
from .models import Entity


class RelatedEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = ('id', 'name', 'entity_liked', 'description', 'contact', 'reference_person',
                  'reference_person_contact', 'comments')
