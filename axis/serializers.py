from rest_framework import serializers

from attendance.serializers import AttendanceSerializer
from documents.related_serializer import RelatedDocumentSerializer
from entities.related_serializers import RelatedEntitySerializer
from users.related_serializer import RelatedUserSerializer
from .models import Axis


class AxisSerializer(serializers.ModelSerializer):
    users = RelatedUserSerializer(many=True, read_only=False, required=False)
    attendance_axis = AttendanceSerializer(many=True, read_only=False, required=False)
    associated_axes = RelatedEntitySerializer(many=True, read_only=False, required=False)
    document_axis = RelatedDocumentSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Axis
        fields = '__all__'
