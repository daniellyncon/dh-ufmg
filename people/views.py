from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_field = ('assisted', 'document', 'responsible_advisor', 'responsible_intern', 'gender_identity',
                       'preferred_pronouns', 'related_case_bond', 'related_law_suit_bond', )
