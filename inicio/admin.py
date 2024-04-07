from django.contrib import admin
from .models import Inicio

# Register your models here.
@admin.register(Inicio)

class InicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'imagem')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao')
    list_per_page = 10
    list_filter = ('titulo', 'descricao')
    list_editable = ('imagem',)

