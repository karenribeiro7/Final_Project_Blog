from django.contrib import admin
from .models import criarPostagem

@admin.register(criarPostagem)

class criarPostagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'mensagem', 'imagem')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'mensagem')
    list_per_page = 10
    list_filter = ('titulo', 'mensagem')
    list_editable = ('imagem',)