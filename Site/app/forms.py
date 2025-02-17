# forms.py

from django import forms
from .models import Formulario, FormularioTel, FormularioPes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['campo1', 'campo2', 'opcao_pagamento']


class FormularioTelForm(forms.ModelForm):
    class Meta:
        model = FormularioTel
        fields = ['name', 'tel']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tel'].help_text = "Formato +55 xx xxxx-xxxx"

class Waterform(forms.ModelForm):
    class Meta:
        model = FormularioPes
        fields = ['name', 'age', 'weight']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

