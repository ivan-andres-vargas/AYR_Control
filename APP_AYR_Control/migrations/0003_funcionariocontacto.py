# Generated by Django 4.1.6 on 2023-02-01 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("APP_AYR_Control", "0002_representantelegal"),
    ]

    operations = [
        migrations.CreateModel(
            name="FuncionarioContacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombres", models.CharField(max_length=255)),
                ("apellidos", models.CharField(max_length=255)),
                (
                    "tipo_documento",
                    models.CharField(
                        choices=[
                            ("CC", "Cedula de Ciudadanía"),
                            ("CE", "Cedula de Extranjería"),
                        ],
                        max_length=2,
                    ),
                ),
                ("numero_documento", models.CharField(max_length=15)),
                ("fecha_expedicion", models.DateField()),
                ("lugar_expedicion", models.CharField(max_length=255)),
                ("direccion", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("telefono", models.CharField(max_length=15)),
                ("extension", models.CharField(max_length=15)),
                ("celular", models.CharField(max_length=15)),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="APP_AYR_Control.cliente",
                    ),
                ),
            ],
        ),
    ]
