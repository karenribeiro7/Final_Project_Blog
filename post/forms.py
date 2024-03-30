from django import forms
from .models import criarPostagem  


class PostForm(forms.ModelForm):
    class Meta:
        model = criarPostagem   
        fields = ['titulo', 'mensagem', 'categoria', 'autor']