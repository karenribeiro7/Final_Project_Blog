from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import Post as criarPost
from post.forms import PostForm, ComentarioForm
from categorias.models import Categoria


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
            return redirect('criar_postagem')
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

def listar_postagens(request):    
    return render(request, 'galeria/lista_postagens.html')
   

class PostagemViewSet(ModelViewSet):
    queryset = criarPost.objects.all()
    serializer_class = PostSerializer
