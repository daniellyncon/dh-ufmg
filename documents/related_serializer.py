from rest_framework import serializers
from .models import Document


class RelatedDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'type', 'date', 'recipients', 'link')
