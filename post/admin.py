from django import forms
from django.contrib import admin
from post.models import Post

@admin.register(Post)
class criarPostagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'dt_criacao', 'imagem']
    search_fields = ['titulo', 'categoria']
    list_per_page = 8
    list_editable = ['imagem']
    prepopulated_fields = {'slug': ('titulo',)}