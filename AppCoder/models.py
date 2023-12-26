from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()
    celular = models.IntegerField()

class Categorias(models.Model):
    nombre = models.CharField(max_length=40)