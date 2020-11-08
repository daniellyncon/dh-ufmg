from drf_writable_nested import WritableNestedModelSerializer

from cases.related_serializer import RelatedCaseSerializer
from judicial_appeals.serializers import JudicialAppealSerializer
from people.related_serializer import RelatedPersonSerializer
from .models import LawSuit


class LawSuitSerializer(WritableNestedModelSerializer):
    judicial_appeals = JudicialAppealSerializer(many=True, read_only=False, required=False)
    related_people = RelatedPersonSerializer(many=True, read_only=False, required=False)
    case_law_suits = RelatedCaseSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = LawSuit
        fields = ('id', 'law_suit_number', 'action_type', 'open_mandate', 'district', 'law_area', 'latest_moves',
                  'has_lawyer', 'lawyer_name', 'lawyer_contact', 'followed_by_daj', 'minhadaj_number',
                  'start_date', 'transit_date', 'related_people', 'judicial_appeals', 'case_law_suits')



