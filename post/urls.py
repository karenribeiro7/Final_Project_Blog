from django.urls import path
from .views import postagem, postagemdousuario

urlpatterns = [
    path('postagem/', postagem),
    path('postagem/<int:id>', postagem),
    path('areadousuario/postagens/', postagemdousuario, name='postagemdousuario')
]