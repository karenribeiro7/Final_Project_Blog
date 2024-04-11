from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    is_super_user = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome} : {self.email} - {self.data}'

    class Meta:
        verbose_name = 'Formulario de cadastro'
        verbose_name_plural = 'Formularios de cadastro'
        ordering = ['-data']

class Login(models.Model):
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)
