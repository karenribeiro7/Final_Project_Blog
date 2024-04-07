from django.urls import path
from cadastro.views import cadastrar

urlpatterns = [
    path('cadastro/', cadastrar, name='cadastrar'),
]