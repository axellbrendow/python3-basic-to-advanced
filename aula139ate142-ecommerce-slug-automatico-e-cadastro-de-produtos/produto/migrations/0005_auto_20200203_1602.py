# Generated by Django 3.0.3 on 2020-02-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_descricao_longa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao_longa',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]