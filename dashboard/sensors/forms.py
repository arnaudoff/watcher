from django import forms

from dashboard.sensors.models import Sensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = [
            "name"
        ]
