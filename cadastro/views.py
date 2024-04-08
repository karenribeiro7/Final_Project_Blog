from django.shortcuts import render, redirect
from .models import Cadastro
from .forms import CadastroForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages 
from django.http import HttpResponse

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.') 
            return redirect('login')
    else:
        form = CadastroForm()   
    return render(request, 'galeria/cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('senha')
            user = authenticate(request, email=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('paineldousuario.html') 
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.') 
        else:
            messages.error(request, 'Por favor, preencha todos os campos corretamente.')  
    else:
        form = LoginForm()
    return render(request, 'galeria/login.html', {'form': form})

def logout (request):
    logout(request)
    return redirect('galeria/inicio.html')

