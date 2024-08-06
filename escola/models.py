from typing import Any
from django.db import models

# Create your models here.
class Escola(models.Model):
    nome=models.CharField(max_length=200)
    local=models.CharField(max_length=200)
    nivel_de_ensino=models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome=models.CharField(max_length=200)
    hora_aula=models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
# criar os models aluno e professor e receber Escola e Materia

