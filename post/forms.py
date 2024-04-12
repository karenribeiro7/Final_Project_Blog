from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):        
    class Meta:
        model = Post
        fields = ['categoria',  'titulo', 'descricao', 'imagem', 'texto']
        list_display = ('id', 'autor', 'texto', 'imagem')
        list_display_links = ('id', 'titulo')
        search_fields = ('autor', 'texto')
        list_filter = ('autor', 'texto')
        list_editable = ('imagem',)

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        list_display = ('id', 'autor', 'texto', 'data')
   
    
       