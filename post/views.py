from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import criarPostagem
from django.views.decorators.cache import cache_page
from post.forms import PostForm

# Create your views here.
def Post(request):
    return render(request, 'postagem.html')

@cache_page(30)
def criar_postagem(request):
    postagem = criarPostagem.objects.all()
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

class PostagemViewSet(ModelViewSet):
    queryset = criarPostagem.objects.all()
    serializer_class = PostSerializer