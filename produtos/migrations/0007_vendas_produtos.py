# Generated by Django 5.1.4 on 2025-01-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_vendas_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendas',
            name='produtos',
            field=models.ManyToManyField(to='produtos.produto'),
        ),
    ]
