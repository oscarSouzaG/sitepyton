# staticpages/forms.py
from django import forms
from .models import RegistroDeUso

class RegistroDeUsoForm(forms.ModelForm):
    class Meta:
        model = RegistroDeUso
        fields = ['nome_motorista','modelo_veiculo', 'placa', 'destino', 'hora_saida', 'km_saida', 'hora_chegada', 'km_chegada']
        widgets = {
            'hora_saida': forms.TimeInput(attrs={'type': 'time'}),
            'hora_chegada': forms.TimeInput(attrs={'type': 'time'}),
        }
