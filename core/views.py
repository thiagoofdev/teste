from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')


def clients(request):
    return render(request, 'clients.html')


def employees(request):
    return render(request, 'employees.html')


def new_report(request):
    return render(request, 'new_report.html')


def new_client(request):
    return render(request, 'new_client.html')


def new_employee(request):
    return render(request, 'new_employee.html')
