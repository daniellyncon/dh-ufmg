from drf_writable_nested import WritableNestedModelSerializer
from documents.related_serializer import RelatedDocumentSerializer
from entities.related_serializers import RelatedEntitySerializer
from law_suits.related_serializers import RelatedLawSuitSerializer
from people.related_serializer import RelatedPersonSerializer
from tasks.related_serializer import RelatedTaskSerializer
from djoser.serializers import UserSerializer
from axis.serializers import AxisSerializer
from .models import Case


class CaseSerializer(WritableNestedModelSerializer):
    axis = AxisSerializer(many=False, read_only=False, required=False)
    advisor = UserSerializer(many=True, read_only=False, required=False)
    intern = UserSerializer(many=True, read_only=False, required=False)
    assisted_person = RelatedPersonSerializer(many=True, read_only=False, required=False)
    entities = RelatedEntitySerializer(many=True, read_only=False, required=False)
    law_suits = RelatedLawSuitSerializer(many=True, read_only=False, required=False)
    tasks = RelatedTaskSerializer(many=True, read_only=False, required=False)
    documents = RelatedDocumentSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Case
        fields = ('related_areas', 'registration_date', 'reference_contacts', 'daj_number', 'daj_advisor', 'daj_intern',
                  'advisor', 'intern', 'axis', 'entities', 'assisted_person', 'law_suits', 'report', 'tasks',
                  'id', 'documents', 'solution_date')

