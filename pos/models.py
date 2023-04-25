
# Create your models here.
from django.db import models
from datetime import datetime

class Producto(models.Model):
    codigo = models.CharField(max_length=255, unique=True, null=True, blank= True)
    descripcion = models.CharField(max_length=200, null=False)
    imagen = models.ImageField(upload_to='productos', null=True,blank=True)
    costo= models.DecimalField(max_digits=20,decimal_places=2, null=False)
    precio= models.DecimalField(max_digits=20,decimal_places=2, null=False, default=0, blank=True)
    cantidad= models.DecimalField(max_digits=15,decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    def __str__(self):
        return self.descripcion
    

class Cliente(models.Model):
    codigo = models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='clientes'
        verbose_name_plural= 'clientes'

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name= 'Tipo'
        verbose_name_plural= 'Tipos'



class Personal(models.Model):
    tipo= models.ForeignKey(Tipo, on_delete=models.CASCADE)
    documento = models.CharField(max_length=200, null=True, blank=False)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Personals'
        verbose_name_plural= 'personal'

    def __str__(self):
        return self.nombre
