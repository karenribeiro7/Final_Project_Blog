from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import Post as criarPost
from post.forms import PostForm, ComentarioForm
from categorias.models import Categoria
from inicio.views import inicio
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def postagem_detalhada(request, pk):
    postagem = criarPost.objects.get(pk=pk)
    contexto = {
        'postagem': postagem
    }
    return render(request, 'postagem_detalhada.html', contexto)

def gerenciar_postagem(request):
    postagens_usuario = criarPost.objects.filter(usuario=request.user)
    contexto = {
        'postagens_usuario': postagens_usuario
    }
    return render(request, 'postagemdousuario.html', contexto)


@login_required
def editar_postagem(request, pk):
    postagem = criarPost.objects.get(pk=pk)
    form = PostForm(request.POST or None, instance=postagem)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
        return redirect('postagem_detalhada', pk=postagem.pk)
    contexto = {
        'postagem': postagem,
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'editar_postagem.html', contexto)
 
 
def criar_postagem(request):
    template_name = 'criar_postagem.html'
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
        messages.success(request, 'A postagem foi excluída com sucesso.')
        return redirect('gerenciar_postagem')
    return render(request, 'postagemdousuario.html')

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
    return render(request, 'postagem_detalhada.html', contexto)

def listar_postagens(request):    
    return render(request, 'lista_postagens.html')
   

class PostagemViewSet(ModelViewSet):
    queryset = criarPost.objects.all()
    serializer_class = PostSerializer

def buscar_posts(request):
    if request.method == "POST":
        searched = request.POST['searched'] # tentar tbm com () se der errado
        postagens = criarPost.objects.filter(titulo__contains=searched) # se "icontains" der errado usar só "contains", icontains serve para não fazer distinção entre maiúsculo/minúsculo
        return render(request, 'resultado_busca.html', {'searched': searched, 'postagens': postagens})
    else: 
        return render(request, 'resultado_busca.html')
