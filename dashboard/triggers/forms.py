from django import forms

from dashboard.triggers.models import Trigger

class TriggerForm(forms.ModelForm):
    class Meta:
        model = Trigger
        fields = [
            "time_triggered"
        ]
