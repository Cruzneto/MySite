# No arquivo views.py do seu aplicativo


# views.py

from app.models import Item, Formulario, FormularioTel, FormularioPes
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormularioForm, FormularioTelForm, Waterform
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from datetime import datetime
import random
from time import time
import requests


def minha_view(request):
    now = datetime.now().time()
    print("Hora atual:", now)  # For debug

    morning = datetime.strptime('12:00', '%H:%M').time()  # Changed from 12:00 to 06:00
    afternoon = datetime.strptime('18:00', '%H:%M').time()
    
    greeting = ""

    if now < morning:
        greeting = "Bom dia"
    elif now < afternoon:
        greeting = "Boa tarde"
    else:
        greeting = "Boa noite"

    print("Saudação determinada:", greeting)  # For debug
    return render(request, 'meu_template.html', {'greeting': greeting})

def cadastrar_formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')
    else:
        form = FormularioForm()
    return render(request, 'formulario.html', {'form': form})

def item_list(request):
    items = Formulario.objects.all()
    return render(request, 'cadastros.html', {'items': items})

#Formulario 2
def cadastrar_formulario2(request):
    if request.method == 'POST':
        form = FormularioTelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')
    else:
        form = FormularioTelForm()
    return render(request, 'formulario_tel.html', {'form': form})

def parcelado_list(request):
    # Filtrar os cadastros que têm a opção de pagamento "parcelado"
    itens_parcelados = Formulario.objects.filter(opcao_pagamento='parcelado')
    return render(request, 'lista_p.html', {'itens_parcelados': itens_parcelados})


def water_list(request):
    items = FormularioPes.objects.all()
    return render(request, 'water.html', {'items': items})

def name_list(request):
    names = FormularioPes.objects.values_list('name', flat=True)
    print(names)
    return render(request, 'lista_nomes.html', {'names': names})
    
def detalhes_pessoa(request, name):
    pessoa = get_object_or_404(FormularioPes, name=name)
    return render(request, 'detalhes_pessoa.html', {'pessoa': pessoa})

    
def app_agua(request):
    if request.method == 'POST':
        form = Waterform(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            peso_corporal = form_instance.weight
            quantidade_litros = calcular_quantidade_agua(peso_corporal)
            form_instance.quantidade_agua = quantidade_litros  # Atribui a quantidade de água calculada ao campo quantidade_agua
            form_instance.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')
    else:
        form = Waterform()
    return render(request, 'formulario.html', {'form': form})

# Função para calcular a quantidade de água necessária
def calcular_quantidade_agua(peso_corporal):
    print(peso_corporal)
    return float(peso_corporal) * 0.050

def calculadora(request):
    if request.method == 'POST':
        # Recebe os valores dos campos do formulário
        operacao = request.POST.get('operacao')
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))

        # Realiza a operação solicitada
        if operacao == 'soma':
            resultado = num1 + num2
        elif operacao == 'subtracao':
            resultado = num1 - num2
        elif operacao == 'multiplicacao':
            resultado = num1 * num2
        elif operacao == 'divisao':
            if num2 != 0:  # Evita a divisão por zero
                resultado = num1 / num2
            else:
                resultado = 'Erro: Divisão por zero'
        else:
            resultado = 'Operação inválida'

        # Retorna o resultado em formato JSON
        return JsonResponse({'resultado': resultado})

    return render(request, 'calculadora.html')


def get_exchange_rate():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']['BRL']

def convert_currency(request):
    if request.method == 'GET':
        amount = float(request.GET.get('amount', 1))
        exchange_rate = get_exchange_rate()
        converted_amount = amount * exchange_rate
        return JsonResponse({'amount': amount, 'converted_amount': converted_amount, 'rate': exchange_rate})


def converter(request):
    return render(request, 'conversor.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def damage(request):
    return random.randint(1, 100)
