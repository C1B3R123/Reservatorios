from django.db import models

class Reservatorio(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.FloatField()
    nivel_atual = models.FloatField()
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    status_bomba = models.CharField(
        max_length=20,
        choices=[('Ligada', 'Ligada'), ('Desligada', 'Desligada'), ('Quebrada', 'Quebrada')],
        default='Desligada'
    )

    @property
    def altura_agua(self):
        if self.capacidade > 0:
            return (self.nivel_atual / self.capacidade) * 100
        return 0

    @property
    def estado(self):
        if self.nivel_atual >= self.capacidade * 0.75:
            return "Cheio"
        elif self.nivel_atual >= self.capacidade * 0.25:
            return "Metade"
        return "Vazio"

    def __str__(self):
        return self.nome
