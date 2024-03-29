# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#  EMPLEADOS  
class Empleado(models.Model):
    nombre = models.CharField(max_length=50, blank=True, default='')
    apaterno = models.CharField(max_length=50, blank=True, default='')
    amaterno = models.CharField(max_length=50, blank=True, default='')
    fechanac = models.DateField()
    email = models.EmailField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.email + ', ' + self.nombre + ' ' + self.apaterno + ' ' + self.amaterno

#  CLIENTES  
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=True, default='')
    direccion = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre + ', ' + self.direccion + ' ' + self.email + ' ' + self.telefono

#  AREAS  
class Area(models.Model):
    area = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.area

#  PEDIDOS  
class Pedido(models.Model):
    fecha_pedido = models.DateField()
    fecha_envio = models.DateField()
    id_cliente = models.ForeignKey(Cliente)
    id_empleado = models.ForeignKey(Empleado)

    def __str__(self):
        return self.fecha_pedido + ', ' + self.fecha_envio + ' ' + self.id_cliente + ' ' + self.id_empleado

#  AREAS CLIENTE  
class AreaCliente(models.Model):
    no_empleados = models.IntegerField()
    id_area = models.ForeignKey(Area)
    id_cliente = models.ForeignKey(Cliente)

    def __str__(self):
        return self.no_empleados + ', ' + self.id_area + ', ' + self.id_cliente

#  PRODUCTOS  
class Producto(models.Model):
    producto = models.CharField(max_length=100, blank=True, default='')
    costo = models.FloatField()
    precio = models.FloatField()
    existencia = models.IntegerField()
    reorden = models.IntegerField()
    comprometidas = models.IntegerField()
    vigente = models.BooleanField()
    imagen = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.producto + ', ' + self.costo + ', ' + self.precio + ', ' + self.existencia + ', ' + self.reorden + ', ' + self.comprometidas + ', ' + self.vigente + ', ' + self.imagen

#  PRODUCTOS AREAS CLIENTE  
class ProductoAreaCliente(models.Model):
    consumo = models.IntegerField()
    id_area_cliente = models.ForeignKey(AreaCliente)
    id_producto = models.ForeignKey(Producto)

    def __str__(self):
        return self.consumo + ', ' + self.id_area_cliente + ', ' + self.id_producto

#  DETALLE PEDIDO 
class DetallePedido(models.Model):
    precio = models.FloatField()
    descuento = models.FloatField()
    cantidad = models.FloatField()
    id_producto = models.ForeignKey(Producto)
    id_pedido = models.ForeignKey(Pedido)

    def __str__(self):
        return self.precio + ', ' + self.descuento + ', ' + self.cantidad + ', ' + self.id_producto + ', ' + self.id_pedido