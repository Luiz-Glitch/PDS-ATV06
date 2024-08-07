from django.urls import path
from .views import *

urlpatterns = [
    path('luiz/', luiz, name='home'),
    path('joao/', joao, name='home'),
]