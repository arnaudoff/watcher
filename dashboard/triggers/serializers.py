from rest_framework import serializers

from dashboard.triggers.models import Trigger

class TriggerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        sensor = validated_data.pop('sensor_id')
        trigger = Trigger.objects.create(sensor=sensor, **validated_data)
        return trigger

    class Meta:
        model = Trigger
        fields = ('time_triggered', 'image', 'sensor_id')
