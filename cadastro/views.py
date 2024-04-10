from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from cadastro.models import Cadastro, Login
from cadastro.serializers import CadastroSerializer, LoginSerializer
from cadastro.forms import CadastroForm
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def paineldousuario(request):
    usuario = request.user
    dados_usuario = {}
    if usuario.is_authenticated:
        dados_usuario = {
            'nome': usuario.username,
            'email': usuario.email,
        }
    return render(request, 'galeria/paineldousuario.html', {'usuario': dados_usuario})

def gerenciar_perfil(request):
    usuario = request.user
    if usuario.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            usuario.email = email
            usuario.save()
            messages.success(request, 'Perfil atualizado com sucesso')
    return render(request, 'galeria/gerenciar_perfil.html', {'usuario': usuario})

@cache_page(30)
def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.save()
            return redirect('paineldousuario')
    else:
        form = CadastroForm()
    return render(request, 'galeria/cadastro.html', {'form': form})

 
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            usuario = Cadastro.objects.get(email=email)
            if usuario.senha == senha:
                return redirect('paineldousuario')
            else:
                messages.error(request, 'Senha incorreta')
        except Cadastro.DoesNotExist:
            messages.error(request, 'Usuária não encontrada')
    return render(request, 'galeria/login.html')

@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')


class cadastroModelViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class loginModelViewSet(ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
