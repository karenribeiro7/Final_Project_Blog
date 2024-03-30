from django.urls import path
from .import views

app_name = 'post'

urlpatterns = [
     path('cria_postagem/', views.cria_postagem, name='cria_postagem'),
     path('', views.lista_postagem, name='lista_postagem'),
     path('<int:postagem_id>/editar/', views.edita_postagem, name='edita_postagem'), 
     path('excluir_postagem/<int:postagem_id>/', views.exclui_postagem, name='exclui_postagem')   
]