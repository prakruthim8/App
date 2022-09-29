from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='manu'),
    path('calculations', views.calculation , name='calculation')
]