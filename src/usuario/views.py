from venv import logger
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from usuario.forms import CadastroForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User

def logout_user(request):
    logout(request)
    return redirect('login')

def paineldousuario(request):
    usuario = request.user
    dados_usuario ={}
    if usuario.is_authenticated:
        dados_usuario = {
           'id': usuario.id,
            'username': usuario.username,
            'email': usuario.email,
        }
    return render(request, 'paineldousuario.html', {'usuario': dados_usuario} )

def cadastro_user(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                logger.info(f'Usuário (a) {user.username} autenticado com sucesso após o cadastro')
                return redirect('paineldousuario')
            else:
                logger.error('Erro !!! Usuário não autenticado após o cadastro')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('paineldousuario')  # Redireciona para a página paineldousuario
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

    
def gerenciar_perfil(request):
    usuario = request.user
    if usuario.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            usuario.email = email
            usuario.save()
            messages.success(request, 'Perfil atualizado com sucesso')
    return render(request, 'gerenciar_perfil.html', {'usuario': usuario})