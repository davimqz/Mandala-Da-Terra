# Generated by Django 5.1.2 on 2024-10-17 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culturas', '0006_plantacao_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantacao',
            old_name='data_colheita',
            new_name='data_plantacao',
        ),
    ]