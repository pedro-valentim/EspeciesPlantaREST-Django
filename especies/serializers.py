from especies.models import Especie
from rest_framework import serializers


class EspecieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especie
        fields = (
            'nomeCientifico',
            'genero',
            'especie',
            'nomePopular',
            'exotica',
            'classe',
            'familia',
            'nomeAutor',
            'tipo',
            'dataCadastro'
        )
