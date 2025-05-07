from django import forms
from .models import Reservoir

class ReservoirForm(forms.ModelForm):
    class Meta:
        model = Reservoir
        fields = ['name', 'capacity', 'current_level', 'pump_status', 'latitude', 'longitude', 'address']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
