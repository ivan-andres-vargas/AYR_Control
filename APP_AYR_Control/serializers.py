from rest_framework import serializers
from .models import Cliente, RepresentanteLegal, FuncionarioContacto


# Serializers que definen la representación de los datos de los modelos, Clase Cliente.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


# Serializers que definen la representación de los datos de los modelos, Clase RepresentanteLegal.
class RepresentanteLegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepresentanteLegal
        fields = '__all__'


# Serializers que definen la representación de los datos de los modelos, Clase FuncionarioContacto.
class FuncionarioContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioContacto
        fields = '__all__'




