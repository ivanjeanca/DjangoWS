# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from . models import Empleado
from . models import Cliente
from . models import Area
from . models import Pedido
from . models import AreaCliente
from . models import Producto
from . models import ProductoAreaCliente
from . models import DetallePedido
from . serializers import EmpleadoSerializer
from . serializers import ClienteSerializer
from . serializers import AreaSerializer
from . serializers import PedidoSerializer
from . serializers import AreaClienteSerializer
from . serializers import ProductoSerializer
from . serializers import ProductoAreaClienteSerializer
from . serializers import DetallePedidoSerializer


###############
#  EMPLEADOS  #
###############

@csrf_exempt
def EmpleadoAPI(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpleadoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def EmpleadoAPI_ID(request, pk):
    try:
        empleado = Empleado.objects.get(pk = pk)
    except Empleado.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmpleadoSerializer(empleado, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        empleado.delete()
        return HttpResponse(status = 204)


##############
#  CLIENTES  #
##############

@csrf_exempt
def ClienteAPI(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def ClienteAPI_ID(request, pk):
    try:
        cliente = Cliente.objects.get(pk = pk)
    except Cliente.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(cliente, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        cliente.delete()
        return HttpResponse(status = 204)


###########
#  AREAS  #
###########

@csrf_exempt
def AreaAPI(request):
    if request.method == 'GET':
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AreaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def AreaAPI_ID(request, pk):
    try:
        area = Area.objects.get(pk = pk)
    except Area.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = AreaSerializer(area)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AreaSerializer(area, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        area.delete()
        return HttpResponse(status = 204)


#############
#  PEDIDOS  #
#############

@csrf_exempt
def PedidoAPI(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PedidoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def PedidoAPI_ID(request, pk):
    try:
        pedido = Pedido.objects.get(pk = pk)
    except Pedido.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PedidoSerializer(pedido, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        pedido.delete()
        return HttpResponse(status = 204)


###################
#  AREAS CLIENTE  #
###################

@csrf_exempt
def AreaCliente(request):
    if request.method == 'GET':
        areascliente = AreaCliente.objects.all()
        serializer = AreaClienteSerializer(areascliente, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AreaClienteSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def AreaCliente_ID(request, pk):
    try:
        areacliente = AreaCliente.objects.get(pk = pk)
    except AreaCliente.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = AreaClienteSerializer(areacliente)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AreaClienteSerializer(areacliente, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        areacliente.delete()
        return HttpResponse(status = 204)


###############
#  PRODUCTOS  #
###############

@csrf_exempt
def ProductoAPI(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def ProductoAPI_ID(request, pk):
    try:
        producto = Producto.objects.get(pk = pk)
    except Producto.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        producto.delete()
        return HttpResponse(status = 204)


###########################
#  PRODUCTO AREA CLIENTE  #
###########################

@csrf_exempt
def ProductoAreaClienteAPI(request):
    if request.method == 'GET':
        productosareacliente = ProductoAreaCliente.objects.all()
        serializer = ProductoAreaClienteSerializer(productosareacliente, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoAreaClienteSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def ProductoAreaClienteAPI_ID(request, pk):
    try:
        productoareacliente = ProductoAreaCliente.objects.get(pk = pk)
    except ProductoAreaCliente.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = ProductoAreaClienteSerializer(productoareacliente)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoAreaClienteSerializer(productoareacliente, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        productoareacliente.delete()
        return HttpResponse(status = 204)


####################
#  DETALLE PEDIDO  #
####################

@csrf_exempt
def DetallePedidoAPI(request):
    if request.method == 'GET':
        detallepedidos = DetallePedido.objects.all()
        serializer = DetallePedidoSerializer(detallepedidos, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetallePedidoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def DetallePedidoAPI_ID(request, pk):
    try:
        detallepedido = DetallePedido.objects.get(pk = pk)
    except DetallePedido.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = DetallePedidoSerializer(detallepedido)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetallePedidoSerializer(detallepedido, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        detallepedido.delete()
        return HttpResponse(status = 204)
