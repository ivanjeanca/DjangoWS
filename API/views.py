# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from . models import Empleado, Cliente, Area, Pedido, AreaCliente, Producto, ProductoAreaCliente, DetallePedido
from . serializers import EmpleadoSerializer, ClienteSerializer, AreaSerializer, PedidoSerializer, AreaClienteSerializer, ProductoSerializer, ProductoAreaClienteSerializer, DetallePedidoSerializer

#  EMPLEADOS
class EmpleadoList(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

#  CLIENTES
class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

#  AREAS
class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

#  PEDIDOS
class PedidoList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

#  AREAS CLIENTE
class AreaClienteList(generics.ListCreateAPIView):
    queryset = AreaCliente.objects.all()
    serializer_class = AreaClienteSerializer

class AreaClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaCliente.objects.all()
    serializer_class = AreaClienteSerializer

#  PRODUCTOS
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#  PRODUCTOS AREA CLIENTE
class ProductoAreaClienteList(generics.ListCreateAPIView):
    queryset = ProductoAreaCliente.objects.all()
    serializer_class = ProductoAreaClienteSerializer

class ProductoAreaClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductoAreaCliente.objects.all()
    serializer_class = ProductoAreaClienteSerializer

#  DETALLE PEDIDO
class DetallePedidoList(generics.ListCreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class DetallePedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer