from django.contrib import admin
from .models import criarPostagem

# Register your models here.
@admin.register(criarPostagem)

class criarPostagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'imagem')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao')
    list_per_page = 10
    list_filter = ('titulo', 'descricao')
    list_editable = ('imagem',)