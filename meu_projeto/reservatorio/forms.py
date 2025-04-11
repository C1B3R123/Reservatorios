from django import forms
from .models import Reservatorio

class ReservatorioForm(forms.ModelForm):
    class Meta:
        model = Reservatorio
        fields = ['nome', 'capacidade', 'nivel_atual', 'status_bomba']
        