# Generated by Django 3.1 on 2020-08-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0004_remove_avaliacao_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='resenha',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
