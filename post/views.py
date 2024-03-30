from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import Postagem
from django.views.decorators.cache import cache_page
from post.forms import PostForm
from django.shortcuts import get_object_or_404

def Post(request):
    return render(request, 'postagem.html')

@cache_page(30)
def criar_postagem(request):
    postagem = Postagem.objects.all()
    form = PostForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'criar_postagem.html', contexto)

def lista_postagem(request):
    postagens = Postagem.objects.all()
    return render(request, 'lista_postagens')

def editar_postagem(request, pk):
    postagem = Postagem.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=postagem)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'criar_postagem.html', contexto)
                    
def excluir_postagem(request, postagem_id):
    postagem = Postagem.get_object_or_404(Postagem, pk=postagem_id)
    postagem.delete()
    return render(request, 'excluir_postagem', {'postagem': Postagem.objects.all()})

class PostagemViewSet(ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostSerializer