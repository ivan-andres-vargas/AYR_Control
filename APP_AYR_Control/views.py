from rest_framework import viewsets, request
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ClienteSerializer, RepresentanteLegalSerializer, FuncionarioContactoSerializer
from .models import Cliente, RepresentanteLegal, FuncionarioContacto, SimulacionCredito

import numpy as np
from django.shortcuts import render, redirect


# Para realizar operaciones de CRUD, modelo Cliente.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# Para realizar operaciones de CRUD, modelo RepresentanteLegal.
class RepresentanteLegalViewSet(viewsets.ModelViewSet):
    queryset = RepresentanteLegal.objects.all()
    serializer_class = RepresentanteLegalSerializer


# Para realizar operaciones de CRUD, modelo FuncionarioContacto.
class FuncionarioContactoViewSet(viewsets.ModelViewSet):
    queryset = FuncionarioContacto.objects.all()
    serializer_class = FuncionarioContactoSerializer


# Función para calcular la tasa efectiva según la forma de pago.
def calcular_tasa_efectiva(tasa_efectiva_anual, forma_pago):
    tasa_efectiva = tasa_efectiva_anual
    if forma_pago == 'diario':
        tasa_efectiva = tasa_efectiva_anual / 365
    elif forma_pago == 'semanal':
        tasa_efectiva = tasa_efectiva_anual / 52
    elif forma_pago == 'quincenal':
        tasa_efectiva = tasa_efectiva_anual / 24
    elif forma_pago == 'mensual':
        tasa_efectiva = tasa_efectiva_anual / 12
    elif forma_pago == 'bimensual':
        tasa_efectiva = tasa_efectiva_anual / 6
    elif forma_pago == 'trimestral':
        tasa_efectiva = tasa_efectiva_anual / 4
    elif forma_pago == 'tetratremestral':
        tasa_efectiva = tasa_efectiva_anual / 3
    elif forma_pago == 'semestral':
        tasa_efectiva = tasa_efectiva_anual / 2
    return tasa_efectiva




