# Generated by Django 5.1.1 on 2024-11-28 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('tempo_colheita_dias', models.IntegerField(default=90)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rua', models.TextField(default='Rua desconhecida')),
                ('completed', models.BooleanField(default=False)),
                ('data_plantio', models.DateField(blank=True, null=True)),
                ('data_colheita', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantaCompanheira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companheiras', to='crops.cultura')),
            ],
        ),
    ]