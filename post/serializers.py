from rest_framework.serializers import ModelSerializer
from post.models import criarPostagem


class PostSerializer(ModelSerializer):
    class Meta:
        model = criarPostagem
        fields = '__all__'
