# Generated by Django 5.0.4 on 2024-04-25 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_formulario_opcao_pagamento"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormularioPes",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.CharField(max_length=2)),
                ("weight", models.CharField(max_length=3)),
            ],
        ),
    ]
