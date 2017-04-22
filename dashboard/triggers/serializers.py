from rest_framework import serializers

from dashboard.triggers.models import Trigger

class TriggerSerializer(serializers.ModelSerializer):
    sensor = serializers.ReadOnlyField(source='sensor.name')

    class Meta:
        model = Trigger
        fields = ('time_triggered')
