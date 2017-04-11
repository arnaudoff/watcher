from django import forms
from sensors.models import Sensor

class AddSensorForm(forms.ModelForm):
	name = forms.CharField(label="Sensor name", max_length=20)
	active = forms.BooleanField(required=False, initial=True, label="is active")

	class Meta:
		model = Sensor
		fields = [
			'name',
			'active'
		]