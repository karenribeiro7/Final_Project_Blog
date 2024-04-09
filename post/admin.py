from django import forms
from django.contrib import admin
from post.models import Post

@admin.register(Post)
class criarPostagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'texto', 'imagem']
    list_display_links = ['id', 'titulo']
    search_fields = ['titulo', 'texto']
    list_per_page = 10
    list_filter = ['titulo', 'texto']
    list_editable = ['imagem']