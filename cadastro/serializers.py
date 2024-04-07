from rest_framework.serializers import ModelSerializer
from cadastro.models import Cadastro


class CadastroSerializer(ModelSerializer):
    class Meta:
        model = Cadastro
        fields = '__all__'


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ['email', 'senha']
