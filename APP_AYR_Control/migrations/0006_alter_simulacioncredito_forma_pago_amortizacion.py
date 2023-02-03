# Generated by Django 4.1.6 on 2023-02-01 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("APP_AYR_Control", "0005_simulacioncredito"),
    ]

    operations = [
        migrations.AlterField(
            model_name="simulacioncredito",
            name="forma_pago",
            field=models.CharField(
                choices=[
                    ("diario", "Diario"),
                    ("semanal", "Semanal"),
                    ("quincenal", "Quincenal"),
                    ("mensual", "Mensual"),
                    ("bimensual", "Bimensual"),
                    ("trimestral", "Trimestral"),
                    ("tetratremestral", "Tetratremestral"),
                    ("semestral", "Semestral"),
                    ("anual", "Anual"),
                ],
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Amortizacion",
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
                ("numero_cuota", models.PositiveSmallIntegerField()),
                ("capital", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "cuota_variable",
                    models.DecimalField(decimal_places=2, max_digits=15),
                ),
                ("interes", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "abono_a_capital",
                    models.DecimalField(decimal_places=2, max_digits=15),
                ),
                ("otros_cargos", models.DecimalField(decimal_places=2, max_digits=15)),
                ("cuota_total", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "simulacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="APP_AYR_Control.simulacioncredito",
                    ),
                ),
            ],
        ),
    ]
