from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
     path('criar_postagem/', views.criar_postagem, name='criar_postagem'),
     path('', views.lista_postagens, name='lista_postagens'),
     path('excluir_postagem/<int:postagem_id>/', views.excluir_postagem, name='excluir_postagem'),
     path('<int:postagem_id>/', views.exibir_postagem, name='exibir_postagem'),
     path('<int:postagem_id>/editar/', views.editar_postagem, name='editar_postagem'), 

]
