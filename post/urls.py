from django.urls import path
from post.views import criar_postagem, gerenciar_postagem, postagem_detalhada

urlpatterns = [
    path('criar_postagem/', criar_postagem, name='criar_postagem'),
    path('gerenciar_postagem', gerenciar_postagem, name='gerenciar_postagem'), #OK
    path('post/<int:pk>/', postagem_detalhada, name='postagem_detalhada'), #OK
]