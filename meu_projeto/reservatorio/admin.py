from django.contrib import admin
from .models import Reservatorio

class ReservatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade', 'nivel_atual', 'get_altura_agua', 'status_bomba', 'ultima_atualizacao')

    def get_altura_agua(self, obj):
        if obj.capacidade > 0:
            return f"{(obj.nivel_atual / obj.capacidade) * 100:.2f}%"
        return "0%"
    get_altura_agua.short_description = 'Altura da Água'

admin.site.register(Reservatorio, ReservatorioAdmin)
