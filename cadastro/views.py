from django.shortcuts import render

def cadastrar(request):
    return render(request, 'galeria/cadastro.html')

def login(request):
    return render(request, 'galeria/login.html')