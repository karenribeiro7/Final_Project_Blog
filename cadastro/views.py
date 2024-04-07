from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request, 'galeria/cadastro.html')

def login(request):
    return render(request, 'login.html')