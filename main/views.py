from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Vista principal de ThesiCare"""
    return render(request, 'main/home.html')

def about(request):
    """Vista sobre el proyecto"""
    return HttpResponse('<h1>Acerca de ThesiCare</h1><p>Plataforma para gestión de tesis</p>')
