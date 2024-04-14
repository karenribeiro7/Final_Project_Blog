from django.shortcuts import get_object_or_404, render
from post.models import Post
from inicio.models import Squad

# Create your views here.
def inicio(request):
    postagens = Post.objects.order_by('-dt_criacao')    
    return render(request, 'inicio.html', {'postagens': postagens})

def sobre(request):    
    return render(request, 'sobre.html')

def contato(request):
    squads = Squad.objects.all()
    return render(request, 'contato.html', {'squads': squads})

def postagem_detalhes(request, id):
    postagem = get_object_or_404(Post, pk=id)
    return render(request, 'postagem_detalhada.html', {'postagem': postagem})