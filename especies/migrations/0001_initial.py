# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCientifico', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=200)),
                ('nomePopular', models.CharField(max_length=100)),
                ('exotica', models.BooleanField(default=False)),
                ('classe', models.CharField(max_length=100)),
                ('familia', models.CharField(max_length=100)),
                ('nomeAutor', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('nenhum', 'Nenhum'), ('arbustiva', 'Arbustiva'), ('arborea', 'Arb\xf3rea')], default='nenhum', max_length=9)),
                ('dataCadastro', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
