from django.shortcuts import render


# Create your views here.
def postagem(request):
    return render(request, 'galeria/postagem.html')

def postagemdousuario(request):
    return render(request, 'galeria/postagemdousuario.html')