from rest_framework import serializers
from .models import LawSuit


class RelatedLawSuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawSuit
        fields = ('id', 'law_suit_number', 'action_type', 'open_mandate', 'district', 'law_area', 'latest_moves',
                  'has_lawyer', 'lawyer_name', 'lawyer_contact', 'followed_by_daj', 'minhadaj_number',
                  'start_date', 'transit_date')
