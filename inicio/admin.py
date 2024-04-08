from django.contrib import admin
from .models import Inicio

@admin.register(Inicio)

class InicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'imagem')
    list_display_links = ('id', 'titulo')
    search_fields = ['titulo']
    list_per_page = 10
    list_filter = ['titulo']
    list_editable = ['imagem']

