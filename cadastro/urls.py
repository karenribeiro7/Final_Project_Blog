from django.urls import path
from cadastro.views import cadastrar, login

app_name = 'cadastro'
urlpatterns = [path('cadastro/', cadastrar, name='cadastrar'),
               path('login/', login, name='login')
               ]
