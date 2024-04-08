from django.shortcuts import get_object_or_404, render
from categorias.models import Categoria
from inicio.models import Inicio

# Create your views here.
def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'galeria/inicio.html', {'categorias': categorias})

def sobre(request):
    return render(request, 'galeria/sobre.html')

def contato(request):
    return render(request, 'galeria/contato.html')

def listar_postagens(request):
    postagens = Inicio.objects.all()
    return render(request, 'galeria/lista_postagens.html', {'postagens': postagens})

def postagem_detalhes(request, id):
    postagem = get_object_or_404(Inicio, pk=postagem)
    return render(request, 'galeria/postagem_detalhes.html', {'postagem': postagem})