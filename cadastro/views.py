from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cadastro.models import Cadastro, Login
from cadastro.serializers import CadastroSerializer, LoginSerializer


# Create your views here.


def cadastrar(request):
    return render(request, 'galeria/cadastro.html')
<<<<<<< HEAD

=======
>>>>>>> e1ead95411c00d29d6a8717d0b50d9ed9bcfcb6b

def login(request):
    return render(request, 'galeria/login.html')

def usuario(request):
    return render(request, 'galeria/paineldousuario.html')


class cadastroModelViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class loginModelViewSet(ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
