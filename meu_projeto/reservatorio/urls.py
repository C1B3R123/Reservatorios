from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('reservoirs/', views.list_reservoirs, name='list_reservoirs'),
    path('add/', views.add_reservoir, name='add_reservoir'),
    path('edit/<int:pk>/', views.edit_reservoir, name='edit_reservoir'),
    path('delete/<int:pk>/', views.delete_reservoir, name='delete_reservoir'),
    path('manage/', views.manage_reservoirs, name='manage_reservoirs'),
    path('details/<int:pk>/', views.reservoir_details, name='reservoir_details'),
]

CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8000',
    'http://127.0.0.1:8000',
]