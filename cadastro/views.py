from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from cadastro.models import Cadastro, Login
from cadastro.serializers import CadastroSerializer, LoginSerializer
from cadastro.forms import CadastroForm
from django.contrib import messages
from django.contrib.auth import logout as django_logout

def cadastrar(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
        return render(request, 'galeria/paineldousuario.html', {'form': form, 'sucesso': sucesso})
    contexto={
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'galeria/cadastro.html', contexto)   
       
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

def paineldousuario(request):
    return render(request, 'galeria/paineldousuario.html')

def logout(request):
    django_logout(request)
    return redirect('/')


class cadastroModelViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class loginModelViewSet(ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
