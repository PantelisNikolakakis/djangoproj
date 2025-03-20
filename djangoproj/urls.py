from django.urls import path
from . import views

app_name = 'djangoproj'

urlpatterns = [
    path('', views.index, name = 'index')
]