from drf_writable_nested.serializers import WritableNestedModelSerializer
from address.serializers import AddressSerializer
from on_duty.serializers import OnDutySerializer
from axis.serializers import AxisSerializer
from cases.related_serializer import RelatedCaseSerializer
from documents.related_serializer import RelatedDocumentSerializer
from people.related_serializer import RelatedPersonSerializer
from tasks.related_serializer import RelatedTaskSerializer
from .models import User


class UserSerializer(WritableNestedModelSerializer):
    address = AddressSerializer(many=False, required=False)
    duties = OnDutySerializer(many=True, read_only=False, required=False)
    axis = AxisSerializer(many=False, required=False)
    in_charge = RelatedTaskSerializer(many=True, read_only=False, required=False)
    prepared_by = RelatedDocumentSerializer(many=True, read_only=False, required=False)
    advisor = RelatedCaseSerializer(many=True, read_only=False, required=False)
    intern = RelatedCaseSerializer(many=True, read_only=False, required=False)
    p_advisor = RelatedPersonSerializer(many=True, read_only=False, required=False)
    p_intern = RelatedPersonSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'bond_type', 'phone', 'registration', 'course', 'university', 'department',
                  'rg', 'cpf', 'cnh', 'date_joined', 'date_fired', 'is_active', 'scholarship', 'scholarship_type',
                  'address', 'duties', 'in_charge', 'axis', 'prepared_by', 'advisor', 'intern', 'p_advisor', 'p_intern')
        depth = 1

