from django.shortcuts import render
from .models import Categorias, Postagem


def postagem(request):
    categorias = Categorias.objects.all()
    return render(request, 'postagem.html', {'categorias': categorias})

def posts_por_categoria(request, categoria_id):
    categoria = Categorias.objects.get(id=categoria_id)
    posts = Postagem.objects.filter(categoria=categoria).order_by('-data_publicação')
    return render(request, 'posts_por_categoria.html',{'categoria': categoria, 'posts': posts})