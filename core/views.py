from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')


def clients(request):
    return render(request, 'clients.html')


def employees(request):
    return render(request, 'employees.html')
