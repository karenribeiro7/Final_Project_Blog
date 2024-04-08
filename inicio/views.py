from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'galeria/inicio.html')

def sobre(request):
    return render(request, 'galeria/sobre.html')

def contato(request):
    return render(request, 'galeria/contato.html')
