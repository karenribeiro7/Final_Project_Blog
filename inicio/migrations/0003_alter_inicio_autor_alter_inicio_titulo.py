# Generated by Django 4.2.11 on 2024-04-10 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inicio", "0002_inicio_autor_inicio_data_postagem_inicio_imagem_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inicio",
            name="autor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="inicio",
            name="titulo",
            field=models.CharField(max_length=100),
        ),
    ]