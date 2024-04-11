from django.urls import path
from post.views import criar_postagem

urlpatterns = [
    path('criar_postagem/', criar_postagem, name='criar_postagem'),
]