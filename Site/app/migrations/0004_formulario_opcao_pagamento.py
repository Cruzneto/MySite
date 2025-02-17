# Generated by Django 5.0.4 on 2024-04-20 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_formulariotel"),
    ]

    operations = [
        migrations.AddField(
            model_name="formulario",
            name="opcao_pagamento",
            field=models.CharField(
                choices=[("a_vista", "À vista"), ("parcelado", "Parcelado")],
                default="a_vista",
                max_length=10,
            ),
        ),
    ]
