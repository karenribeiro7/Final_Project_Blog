from django import forms
from .models import Cadastro


class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']