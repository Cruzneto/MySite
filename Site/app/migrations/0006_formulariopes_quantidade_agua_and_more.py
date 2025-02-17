# Generated by Django 5.0.4 on 2024-04-30 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_formulariopes"),
    ]

    operations = [
        migrations.AddField(
            model_name="formulariopes",
            name="quantidade_agua",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="formulariopes",
            name="weight",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
