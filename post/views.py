from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer  
from .models import Post


# Create your views here.
def post(request):
    return render(request, 'postagem.html')


class PostagemViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer