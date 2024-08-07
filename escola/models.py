from typing import Any
from django.db import models

# Create your models here.
class Escola(models.Model):
    nome=models.CharField(max_length=200)
    local=models.CharField(max_length=200)
    nivel_de_ensino=models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    data_entrada = models.DateField(auto_now_add=True)
    matricula = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
