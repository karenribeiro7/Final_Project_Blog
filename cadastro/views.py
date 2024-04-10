from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from cadastro.models import Cadastro, Login
from cadastro.serializers import CadastroSerializer, LoginSerializer
from cadastro.forms import CadastroForm
from django.contrib import messages
from django.contrib.auth import logout as django_logout

def paineldousuario(request):
    usuario = request.user
    dados_usuario = {
        'nome': usuario.username,
        'email': usuario.email,
    }
    return render(request, 'galeria/paineldousuario.html', {'usuario': dados_usuario})

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paineldousuario') 
    else:
        form = CadastroForm()
    return render(request, 'galeria/cadastro.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            usuario = Login.objects.get(email=email)
            if usuario.senha == senha:
                return redirect('galeria/paineldousuario.html')
            else:
                messages.error(request, 'Senha incorreta')
        except Login.DoesNotExist:
            messages.error(request, 'Usuário não encontrado')
    return render(request, 'galeria/login.html')

def logout(request):
    django_logout(request)
    return redirect('/')


class cadastroModelViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class loginModelViewSet(ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
