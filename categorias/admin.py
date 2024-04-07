from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']
    prepopulated_fields = {'nome': ('nome',)}