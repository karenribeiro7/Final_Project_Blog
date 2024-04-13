from django import forms
from django.contrib import admin
from post.models import Post, Comentario

@admin.register(Post)
class criarPostagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'dt_criacao', 'usuario', 'imagem']
    search_fields = ['titulo', 'categoria']
    list_per_page = 8
    list_editable = ['imagem']
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Comentario)
class criarComentarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'dt_criacao', 'status']
    search_fields = ['nome', 'post']
    list_editable = ['status']