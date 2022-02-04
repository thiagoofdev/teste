import django


from django.urls import path

from .views import clients, employees, new_client, new_employee, new_report


urlpatterns = [
    path('clientes/', clients, name='clients'),
    path('funcionarios/', employees, name='employees'),
    path('novo-cliente/', new_client, name='new_client'),
    path('novo-funcionario/', new_employee, name='new_employee'),
    path('novo-relatorio/', new_report, name='new_report'),
]