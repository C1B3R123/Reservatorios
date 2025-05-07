from django.contrib import admin
from .models import Reservoir

class ReservoirAdmin(admin.ModelAdmin):  # Renomeado de "ReservatorioAdmin"
    list_display = ('name', 'capacity', 'current_level', 'get_water_height', 'pump_status',)  # Atualizado para os novos nomes

    def get_water_height(self, obj):  # Renomeado de "get_altura_agua"
        if obj.capacity > 0:  # Renomeado de "capacidade"
            return f"{(obj.current_level / obj.capacity) * 100:.2f}%"  # Renomeado de "nivel_atual"
        return "0%"
    get_water_height.short_description = 'Altura da Água'  # Texto visível mantido em português

admin.site.register(Reservoir, ReservoirAdmin)
