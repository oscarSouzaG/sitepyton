from django.contrib import admin
from .models import RegistroDeUso

@admin.register(RegistroDeUso)
class RegistroDeUsoAdmin(admin.ModelAdmin):
    list_display = ('modelo_veiculo', 'placa', 'destino', 'hora_saida', 'km_saida', 'hora_chegada', 'km_chegada')
    search_fields = ('modelo_veiculo', 'placa', 'destino')
