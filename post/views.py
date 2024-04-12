from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import Post as criarPost
from post.forms import PostForm, ComentarioForm
from categorias.models import Categoria
from inicio.views import inicio


# Create your views here.
def postagem_detalhada(request, pk):
    postagem = criarPost.objects.get(pk=pk)
    contexto = {
        'postagem': postagem
    }
    return render(request, 'galeria/postagem_detalhada.html', contexto)

def gerenciar_postagem(request):
    postagem = criarPost.objects.all()
    contexto = {
        'postagem': postagem
    }
    return render(request, 'galeria/postagemdousuario.html', contexto)



def editar_postagem(request, pk):
    template_name = 'galeria/editar_postagem.html'
    categorias = Categoria.objects.all()
    postagem = criarPost.objects.get(pk=pk)
    form = PostForm(instance=postagem)
    sucesso = False
    if request.method == 'POST':
        form = PostForm(request.FILES or None, request.POST or None, instance=postagem)
        print(postagem.pk)
        
        if form.is_valid():
            postagem = form.save(False)
            postagem.usuario = request.user
            postagem.slug = form.cleaned_data['postagem.titulo'].replace(' ', '-').lower()
            postagem = criarPost.objects.create(usuario=postagem.usuario, slug=postagem.slug, titulo=form.cleaned_data['titulo'], descricao=form.cleaned_data['descricao'], texto=form.cleaned_data['texto'], imagem=form.cleaned_data['imagem'], categoria=form.cleaned_data['categoria'])
            postagem.save()
            sucesso = True
            return redirect('postagem_detalhada', pk=postagem.pk)
        else:
            print(form.errors)
            raise Http404
    else:
            form = PostForm(instance=postagem)
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso,
        'categorias': categorias
    }
    return render(request, template_name, contexto)
 
 
def criar_postagem(request):
    template_name = 'galeria/criar_postagem.html'
    categorias = Categoria.objects.all()
    postagem = criarPost.objects.all()
    sucesso = False
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES)
        
        if form.is_valid():
            post = form.save(False)
            post.usuario = request.user
            post.slug = form.cleaned_data['titulo'].replace(' ', '-').lower()
            post.save()
            sucesso = True
            return redirect('postagem_detalhada', pk=post.pk)
        else:
            print(form.errors)
            raise Http404

    
    else:
            form = PostForm()
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso,
        'categorias': categorias
    }
    return render(request, template_name, contexto)

def excluir_postagem(request, pk):
    postagem = criarPost.objects.get(pk=pk)
    if request.method == 'POST':
        postagem.delete()
    return render(request, 'galeria/postagemdousuario.html')

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

def listar_postagens(request):    
    return render(request, 'galeria/lista_postagens.html')
   

class PostagemViewSet(ModelViewSet):
    queryset = criarPost.objects.all()
    serializer_class = PostSerializer
