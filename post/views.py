from django.shortcuts import render


# Create your views here.
def postagem(request):
    return render(request, 'postagem.html')