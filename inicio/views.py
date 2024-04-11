from django.shortcuts import get_object_or_404, render
from categorias.models import Categoria
from inicio.models import Inicio

# Create your views here.
def inicio(request):    
    return render(request, 'galeria/inicio.html')

def sobre(request):    
    return render(request, 'galeria/sobre.html')

def contato(request):
    return render(request, 'galeria/contato.html')

def listar_postagens(request):    
    return render(request, 'galeria/lista_postagens.html')

def postagem_detalhes(request, id):
    postagem = get_object_or_404(Inicio, pk=id)
    return render(request, 'galeria/postagem_detalhes.html', {'postagem': postagem})