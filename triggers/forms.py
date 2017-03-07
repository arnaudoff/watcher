from django import forms

from .models import Trigger

class TriggerForm(forms.ModelForm):
    class Meta:
        model = Trigger
        fields = [
            "time_triggered"
        ]
