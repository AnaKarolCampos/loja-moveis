# Generated by Django 5.1.4 on 2025-01-18 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_remove_venda_preco_venda_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
    ]
