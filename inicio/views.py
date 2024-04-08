from django.shortcuts import render
from categorias.models import Categoria

# Create your views here.
def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'galeria/inicio.html', {'categorias': categorias})

def sobre(request):
    return render(request, 'galeria/sobre.html')

def contato(request):
    return render(request, 'galeria/contato.html')
