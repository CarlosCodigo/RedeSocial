from django.urls import path
from .views import *
from . import views

app_name = 'agenda'

urlpatterns = [
    path('inicioagenda/', views.InicioAgenda.as_view(),name='inicioagenda'),
    path('slc/', views.escolhe, name='cria_agendamento'),#para prepopular select
    path('ajax/load-funcoes', views.load_funcoes, name='ajax_load_funcoes'),#para prepopular select
    path('ok/', AgendaSucesso.as_view(), name='agenda_sucesso'),
]
