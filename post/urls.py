from django.urls import path
from .views import postagem, postagemdousuario, paineldousuario

urlpatterns = [
    path('postagem/', postagem),
    path('postagem/<int:id>', postagem),
    path('areadousuario/postagens/', postagemdousuario, name='postagemdousuario'),
    path('paineldousuario/', paineldousuario, name='paineldousuario')
]