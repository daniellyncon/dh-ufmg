import datetime

from attendance.serializers import AttendanceSerializer
from documents.related_serializer import RelatedDocumentSerializer
from entities.related_serializers import RelatedEntitySerializer
from law_suits.related_serializers import RelatedLawSuitSerializer
from .models import Person
from rest_framework import serializers
from djoser.serializers import UserSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from address.serializers import AddressSerializer
from cases.related_serializer import RelatedCaseSerializer
from .related_serializer import RelatedPersonSerializer


class PersonSerializer(WritableNestedModelSerializer):
    age = serializers.SerializerMethodField()
    address = AddressSerializer(many=False, read_only=False, required=False)
    case_people = RelatedCaseSerializer(many=True, read_only=False, required=False)
    responsible_advisor = UserSerializer(many=True, read_only=False, required=False)
    responsible_intern = UserSerializer(many=True, read_only=False, required=False)
    related_person = RelatedPersonSerializer(many=False, read_only=False, required=False)
    related_law_suit = RelatedLawSuitSerializer(many=True, read_only=False, required=False)
    assisted_persons = RelatedEntitySerializer(many=True, read_only=False, required=False)
    attendance = AttendanceSerializer(many=True, read_only=False, required=False)
    document = RelatedDocumentSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Person
        fields = ('assisted', 'first_appointment_date', 'full_name', 'mother_name', 'civil_registry', 'civil_status',
                  'schooling', 'rg', 'cpf', 'cnh', 'email', 'phone', 'gender_identity', 'preferred_pronouns',
                  'self_identification', 'birthday', 'birth_city', 'birth_state', 'has_health_problem',
                  'which_health_problem', 'receives_assistance', 'which_assistance', 'related_person_bond',
                  'contact_email', 'contact_phone', 'related_case_bond', 'id', 'age', 'case_people', 'address',
                  'responsible_advisor', 'responsible_intern', 'related_person', 'related_law_suit', 'assisted_persons',
                  'attendance', 'document')



    @staticmethod
    def get_age(instance):
        if instance.birthday:
            today = datetime.date.today()
            return today.year - instance.birthday.year - ((today.month, today.day) <
                                                          (instance.birthday.month, instance.birthday.day))
        else:
            return ''
