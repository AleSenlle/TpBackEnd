# Generated by Django 5.0.6 on 2024-05-25 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantes', '0004_rename_iimagen_restaurante_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='imagen',
        ),
    ]
