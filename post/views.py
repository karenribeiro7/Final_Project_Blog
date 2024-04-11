from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import Post as criarPost
from django.views.decorators.cache import cache_page
from post.forms import PostForm, ComentarioForm

# Create your views here.
def Post(request):
    return render(request, 'galeria/postagem_detalhada.html')

@cache_page(30)
def criar_postagem(request):    
    postagem = criarPost.objects.all()
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
    return render(request, 'galeria/criar_postagem.html', contexto)

def editar_postagem(request, pk):
    postagem = criarPost.objects.get(pk=pk)
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
    return render(request, 'galeria/criar_postagem.html', contexto)
                    
def excluir_postagem(request, pk):
    postagem = criarPost.objects.get(pk=pk)
    postagem.delete()
    return render(request, 'galeria/postagem.html')

def addcomentario (request, pk):
    postagem = criarPost.objects.get(pk=pk)
    form = ComentarioForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'galeria/postagem_detalhada.html', contexto)
   

class PostagemViewSet(ModelViewSet):
    queryset = criarPost.objects.all()
    serializer_class = PostSerializer
