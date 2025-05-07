from django.db import models

class Reservoir(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.FloatField()
    current_level = models.FloatField()
    pump_status = models.CharField(
        max_length=20,
        choices=[('On', 'Ligada'), ('Off', 'Desligada'), ('Broken', 'Quebrada')],
        default='Off'
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
