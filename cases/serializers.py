from .models import Case
from rest_framework import serializers


class CaseSerializer(serializers.ModelSerializer):
    # assisted_person
    # advisor
    # intern
    # axis
    # entities
    # law_suits
    # tasks
    # documents
    class Meta:
        model = Case
        fields = ['case_number', 'related_areas',  'reference_contacts', 'daj_number',  'daj_advisor',  'daj_intern',
        'report', 'registration_date', 'solution_date']