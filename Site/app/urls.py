# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cadastros', views.item_list, name='item_list'),
    path('', views.minha_view, name='index'),
    path('formulario', views.cadastrar_formulario, name='cadastrar_formulario'),
    path('formulario2', views.cadastrar_formulario2, name='cadastrar_formulario2'),
    path('parcelado', views.parcelado_list, name='parcelado'),
    path('water', views.app_agua, name='water'),
    path('wresult', views.water_list, name='wlist'),
    path('nomes', views.name_list, name='lista_nomes'),
    path('detalhes_pessoa/<str:name>/', views.detalhes_pessoa, name='detalhes_pessoa'),
    path('calculadora', views.calculadora, name='calc'),
    path('conversor', views.converter, name='conversor_dolar'),
    path('api/convert/', views.convert_currency, name='convert_currency'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),


]



