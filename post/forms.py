from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        list_display = ('id', 'autor', 'texto', 'imagem')
        list_display_links = ('id', 'titulo')
        search_fields = ('autor', 'texto')
        list_filter = ('autor', 'texto')
        list_editable = ('imagem',)