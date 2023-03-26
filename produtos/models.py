from django.db import models

# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    quantidade_estoque = models.IntegerField()
    quantidade_critica = models.IntegerField()
    numero_serie = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='produtos')