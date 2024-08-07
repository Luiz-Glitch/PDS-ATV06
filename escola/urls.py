from django.urls import path
from .views import *

urlpatterns = [
    path('joao/', joao, name='home'),
]