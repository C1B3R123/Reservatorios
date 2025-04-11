from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_reservatorios, name='listar_reservatorios'),
    path('adicionar/', views.adicionar_reservatorio, name='adicionar_reservatorio'),
    path('editar/<int:pk>/', views.editar_reservatorio, name='editar_reservatorio'),
    path('deletar/<int:pk>/', views.deletar_reservatorio, name='deletar_reservatorio'),
    path('gerenciar/', views.gerenciar_reservatorios, name='gerenciar_reservatorios'),
]

CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8000',  # Adicione o domínio que você está usando
    'http://127.0.0.1:8000',   # Inclua também o localhost padrão
]