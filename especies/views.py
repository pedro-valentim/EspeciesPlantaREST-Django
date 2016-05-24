# from django.shortcuts import render
from django.http import HttpResponse
from especies.models import Especie
from rest_framework import viewsets
from especies.serializers import EspecieSerializer


def index(request):
    return HttpResponse("Hello, world.")


class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all().order_by('-dataCadastro')
    serializer_class = EspecieSerializer
