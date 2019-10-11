from rest_framework import serializers
from . models import Empleado, Cliente, Area, Pedido, AreaCliente, Producto, ProductoAreaCliente, DetallePedido

#  EMPLEADOS
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apaterno', 'amaterno', 'fechanac', 'email')

#  CLIENTES 
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'direccion', 'email', 'telefono')

#  AREAS  
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'area')

#  PEDIDOS  
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'fecha_pedido', 'fecha_envio', 'id_cliente', 'id_empleado')

#  AREAS CLIENTE  
class AreaClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaCliente
        fields = ('id', 'no_empleados', 'id_area', 'id_cliente')

#  PRODUCTOS  
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'producto', 'costo', 'precio', 'existencia', 'reorden', 'comprometidas', 'vigente', 'imagen')

#  PRODUCTOS AREAS CLIENTE  
class ProductoAreaClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoAreaCliente
        fields = ('id', 'consumo', 'id_area_cliente', 'id_producto')

#  DETALLE PEDIDO  
class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ('id', 'precio', 'descuento', 'cantidad', 'id_producto', 'id_pedido')