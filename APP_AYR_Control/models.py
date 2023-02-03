from django.db import models

# Create your models here.
from django.core.validators import MaxLengthValidator, EmailValidator, RegexValidator


# Modelo de datos para la tabla de clientes.
class Cliente(models.Model):
    TIPO_CHOICES = [
        ('natural', 'Natural'),
        ('juridica', 'Jurídica'),
    ]

    razon_social = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=10)
    nit = models.CharField(max_length=10, validators=[MaxLengthValidator(10), RegexValidator(r'^\d+$')])
    dv = models.CharField(max_length=1, validators=[MaxLengthValidator(1), RegexValidator(r'^\d+$')])
    direccion = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    telefono = models.CharField(max_length=10, validators=[MaxLengthValidator(10), RegexValidator(r'^\d+$')])
    celular = models.CharField(max_length=10, validators=[MaxLengthValidator(10), RegexValidator(r'^\d+$')])
    departamento = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)


# Modelo de datos para la tabla de representantes legales.
class RepresentanteLegal(models.Model):
    empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cedula de Ciudadanía'),
        ('CE', 'Cedula de Extranjería'),
    ]
    tipo_documento = models.CharField(
        max_length=2,
        choices=TIPO_DOCUMENTO_CHOICES,
    )
    numero_documento = models.CharField(max_length=15)
    fecha_expedicion = models.DateField()
    lugar_expedicion = models.CharField(max_length=255)
    direccion = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    extension = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)


# Modelo de datos para la tabla de representantes legales.
class FuncionarioContacto(models.Model):
    empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cedula de Ciudadanía'),
        ('CE', 'Cedula de Extranjería'),
    ]
    tipo_documento = models.CharField(
        max_length=2,
        choices=TIPO_DOCUMENTO_CHOICES,
    )
    numero_documento = models.CharField(max_length=15)
    fecha_expedicion = models.DateField()
    lugar_expedicion = models.CharField(max_length=255)
    direccion = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    extension = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    cargo = models.CharField(max_length=255, default='')
    area = models.CharField(max_length=255, default='')


# Modelo de datos para la tabla de créditos solicitados.
class SimulacionCredito(models.Model):
    FORMAS_PAGO = [
        ('diario', 'Diario'),
        ('semanal', 'Semanal'),
        ('quincenal', 'Quincenal'),
        ('mensual', 'Mensual'),
        ('bimensual', 'Bimensual'),
        ('trimestral', 'Trimestral'),
        ('tetratremestral', 'Tetratremestral'),
        ('semestral', 'Semestral'),
        ('anual', 'Anual'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    representante_legal = models.ForeignKey(RepresentanteLegal, on_delete=models.CASCADE)
    funcionario_de_contacto = models.ForeignKey(FuncionarioContacto, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto_solicitado = models.DecimalField(max_digits=15, decimal_places=2)
    tasa_efectiva_anual = models.DecimalField(max_digits=5, decimal_places=2)
    forma_pago = models.CharField(max_length=20, choices=FORMAS_PAGO)
    tasa_efectiva = models.DecimalField(max_digits=5, decimal_places=2)
    numero_cuotas = models.PositiveSmallIntegerField()
    primera_cuota = models.DateField()
    otros_cargos = models.DecimalField(max_digits=15, decimal_places=2)

