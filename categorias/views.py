from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer
# Create your views here.


def categoria(request):
    return render(request, 'categorias/categoria.html')


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer