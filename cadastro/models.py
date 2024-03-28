from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    is_super_user= models.BooleanField(default=False)

