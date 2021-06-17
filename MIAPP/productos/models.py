from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
#id AutoField -> autoincremental


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    sku = models.IntegerField(unique=True)
    def __str__(self) -> str:
        return f'{self.sku} - {self.nombre}'


class Categoria(models.Model):
    nombre = models.CharField(max_length=10)
    productos = models.ManyToManyField(Producto)