from users.models import User
from on_duty.models import OnDuty
from rest_framework import serializers


class OnDutySerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = OnDuty
        fields = '__all__'
        # fields = ('user', 'day_of_the_week', 'start_time', 'end_time')
