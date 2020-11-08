from rest_framework import serializers
from cases.models import Case


class RelatedCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ('pk', 'related_areas', 'registration_date', 'reference_contacts', 'daj_number', 'daj_advisor',
                  'daj_intern', 'report', 'solution_date')
