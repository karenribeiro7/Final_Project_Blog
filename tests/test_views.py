import pytest
from django.test import RequestFactory
from django.urls import reverse
from cadastro.views import cadastro

@pytest.mark.django_db
def test_cadastro_view():

    factory = RequestFactory()
    
    data = {
        'nome': 'Test User',
        'email': 'test@example.com',
    }

# Cria uma requisição POST com os dados do formulário
    request = factory.post(reverse('cadastro'), data)
    response = cadastro(request)

# Verificações
    assert response.status_code == 200