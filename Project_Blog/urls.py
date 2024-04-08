from django.contrib import admin
from django.urls import path, include
from post.views import postagem
from inicio.views import inicio
from cadastro.views import cadastro, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('postagem/', postagem),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'), 
    path('logout/', logout, name='logout')
]
