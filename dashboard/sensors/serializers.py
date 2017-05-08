from rest_framework import serializers
from dashboard.sensors.models import Sensor

class SensorSerializer(serializers.ModelSerializer):
     class Meta:
         model = Sensor
         fields = ('name', 'timestamp', 'active')
