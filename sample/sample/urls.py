from django.urls import include, path
from django.contrib import admin

from . import views

app_name = 'sample'

urlpatterns = [
    path('', views.index, name='index')
]
