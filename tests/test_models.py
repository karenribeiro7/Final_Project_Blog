import pytest
from django.test import TestCase
from cadastro.models import Cadastro,Login
from django.utils import timezone
from django.db.utils import IntegrityError

#Verificar se os valores foram salvos corretamente
@pytest.mark.django_db
def test_cadastro_salvo_corretamente():

    cadastro = Cadastro.objects.create(
    nome="Teste",
    sobrenome="Usuaria",
    email="teste@example.com",
    senha="senha123",
    data=timezone.now()
)
    assert cadastro.nome == "Teste"
    assert cadastro.sobrenome == "Usuaria"
    assert cadastro.email == "teste@example.com"
    assert cadastro.senha == "senha123"

@pytest.mark.django_db
def test_login_salvo_corretamente():
    login = Login.objects.create(
        email="test@example.com",
        senha="senha123"
    )
    assert login.email == "test@example.com"
    assert login.senha == "senha123"
    