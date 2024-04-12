from django.shortcuts import get_object_or_404, render
from post.models import Post
from inicio.models import Squad

# Create your views here.
def inicio(request):
    postagens = Post.objects.all()    
    return render(request, 'galeria/inicio.html', {'postagens': postagens})

def sobre(request):    
    return render(request, 'galeria/sobre.html')

def contato(request):
    squads = Squad.objects.all()
    return render(request, 'galeria/contato.html', {'squads': squads})

def postagem_detalhes(request, id):
    postagem = get_object_or_404(Post, pk=id)
    return render(request, 'galeria/postagem_detalhada.html', {'postagem': postagem})