from django.urls import path
from .views import gerenciar_perfil, logout_user, paineldousuario

urlpatterns = [
    # Outras URLs da sua aplicação...
    path('logout/', logout_user, name='logout'),
    path('paineldousuario/', paineldousuario, name='paineldousuario'), #OK
    path('gerenciar_perfil/', gerenciar_perfil, name='gerenciar_perfil'), #OK
]