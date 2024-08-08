# staticpages/models.py
from django.db import models

class RegistroDeUso(models.Model):
    nome_motorista = models.CharField(max_length=100)
    modelo_veiculo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    destino = models.CharField(max_length=255)
    hora_saida = models.TimeField()
    km_saida = models.PositiveIntegerField()
    hora_chegada = models.TimeField()
    km_chegada = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.modelo_veiculo} - {self.placa}'
