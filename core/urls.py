import django


from django.urls import path

from .views import clients, employees


urlpatterns = [
    path('clientes/', clients, name='clients'),
    path('funcionarios/', employees, name='employees'),
]