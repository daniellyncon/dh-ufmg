from rest_framework import serializers
from .models import Person


class RelatedPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('assisted', 'first_appointment_date', 'full_name', 'mother_name', 'civil_registry', 'civil_status',
        #           'schooling', 'rg', 'cpf', 'cnh', 'email', 'phone', 'gender_identity', 'preferred_pronouns',
        #           'self_identification', 'birthday', 'birth_city', 'birth_state', 'has_health_problem',
        #           'which_health_problem', 'receives_assistance', 'which_assistance', 'related_person_bond',
        #           'contact_email', 'contact_phone', 'related_case_bond', 'id')
