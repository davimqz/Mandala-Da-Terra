# Generated by Django 5.1.2 on 2024-10-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culturas', '0004_alter_plantacao_ruas_alter_plantacao_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantacao',
            name='data_colheita',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantacao',
            name='data_regada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantacao',
            name='ruas',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='plantacao',
            name='tipo',
            field=models.CharField(max_length=50),
        ),
    ]
