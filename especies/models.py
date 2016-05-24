# -*- coding: utf-8 -*-
from django.utils.encoding import python_2_unicode_compatible
import datetime

from django.db import models
from django.utils import timezone


@python_2_unicode_compatible
class Especie(models.Model):
    nomeCientifico = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    especie = models.CharField(max_length=200)
    nomePopular = models.CharField(max_length=100)
    exotica = models.BooleanField(default=False)
    classe = models.CharField(max_length=100)
    familia = models.CharField(max_length=100)
    nomeAutor = models.CharField(max_length=100)

    nenhum = 'nenhum'
    arbustiva = 'arbustiva'
    arborea = 'arborea'

    tipo_choices = (
        (nenhum, 'Nenhum'),
        (arbustiva, 'Arbustiva'),
        (arborea, 'Arbórea'),
    )

    tipo = models.CharField(max_length=9, choices=tipo_choices, default=nenhum)

    dataCadastro = models.DateTimeField('date published')

    def __str__(self):
        return self.nomeCientifico

    def was_published_recently(self):
        return self.dataCadastro >= timezone.now() - datetime.timedelta(days=1)
