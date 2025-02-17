
# Create your models here.

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django import forms

class Formulario(models.Model):
    OPCOES_PAGAMENTO = [
        ('a_vista', 'À vista'),
        ('parcelado', 'Parcelado'),
    ]

    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=100)
    opcao_pagamento = models.CharField(max_length=10, choices=OPCOES_PAGAMENTO, default='a_vista')

    def __str__(self):
        return f"Formulário {self.id}"

#Pagina de listagem

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

#Formulario 2

class FormularioTel(models.Model):
    name = models.CharField(max_length=100)
    tel = PhoneNumberField()

    def __str__(self):
        return self.name
            
class FormularioPes(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_agua = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Pessoa: {self.name}, Idade: {self.age}, Peso: {self.weight}'

