from pyexpat.errors import messages
from django.shortcuts import render
from flask import redirect
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import criarPostagem
from django.views.decorators.cache import cache_page
from post.forms import PostForm
from django.shortcuts import get_object_or_404

def Post(request):
    return render(request, 'postagem.html')

@cache_page(30)
def cria_postagem(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Postagem criada com sucesso!')
            postagens = criarPostagem.objects.all()
            return render(request, 'lista_postagens.html', {'postagens': postagens}) 
    else:
        form = PostForm()
    return render(request, 'cria_postagem.html', {'form': form})

def lista_postagem(request):
    postagens = criarPostagem.objects.all()
    contexto = {
        'postagens': postagens,
    }
    return render(request, 'postagem.html', contexto)

def edita_postagem(request, postagem_id):
    postagem = get_object_or_404(criarPostagem, pk=postagem_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=postagem)
        if form.is_valid():
            form.save()
            return redirect('lista_postagem')
    else:
        form = PostForm(instance=postagem)
    return render(request, 'edita_postagem.html', {'form': form})
                    
def exclui_postagem(request, postagem_id):
    postagem = criarPostagem.get_object_or_404(criarPostagem, pk=postagem_id)  # trás a postagem a ser excluida ou retorna um erro 404 se não encontrada 
    postagem.delete()                                                #exclui a postagem
    postagens = criarPostagem.objects.all()   # Atualiza o contexto, se necessário
    contexto = {'postagens': postagens}
    return render(request, 'postagem.html', contexto) # Renderiza novamente a página 'postagem.html' com o contexto atualizado

class PostagemViewSet(ModelViewSet):
    queryset = criarPostagem.objects.all()
    serializer_class = PostSerializer