from django.urls import path
<<<<<<< HEAD
from cadastro.views import cadastrar, login

app_name = 'cadastro'
#urlpatterns = [path('cadastro/', cadastrar, name='cadastrar'),
#               path('login/', login, name='login')
#               ]
=======
from cadastro.views import cadastrar

urlpatterns = [
    path('cadastro/', cadastrar, name='cadastrar'),
]
>>>>>>> e1ead95411c00d29d6a8717d0b50d9ed9bcfcb6b
