
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('agendamento/', views.schedulingForm,  name='scheduling-form'),
    path('teste/', views.teste, name='teste')
]
