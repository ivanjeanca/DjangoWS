from rest_framework import serializers
from . models import Empleado
from . models import Cliente
from . models import Area
from . models import Pedido
from . models import AreaCliente
from . models import Producto
from . models import ProductoAreaCliente
from . models import DetallePedido


###############
#  EMPLEADOS  #
###############

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre', 'apaterno', 'amaterno', 'fechanac', 'email']

    id = serializers.IntegerField(read_only = True)
    nombre = serializers.CharField()
    apaterno = serializers.CharField()
    amaterno = serializers.CharField()
    fechanac = serializers.DateField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Empleado.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apaterno = validated_data.get('apaterno', instance.apaterno)
        instance.amaterno = validated_data.get('amaterno', instance.amaterno)
        instance.fechanac = validated_data.get('fechanac', instance.fechanac)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


##############
#  CLIENTES  #
##############

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'direccion', 'email', 'telefono']

    id = serializers.IntegerField(read_only = True)
    nombre = serializers.CharField()
    direccion = serializers.CharField()
    email = serializers.EmailField()
    telefono = serializers.IntegerField()

    def create(self, validated_data):
        return Cliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.email = validated_data.get('email', instance.email)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance


###########
#  AREAS  #
###########

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'area']

    id = serializers.IntegerField(read_only = True)
    area = serializers.CharField()

    def create(self, validated_data):
        return Area.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.area = validated_data.get('area', instance.area)
        instance.save()
        return instance


#############
#  PEDIDOS  #
#############

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'fecha_pedido', 'fecha_envio', 'id_cliente', 'id_empleado']

    id = serializers.IntegerField(read_only = True)
    fecha_pedido = serializers.DateField()
    fecha_envio = serializers.DateField()
    id_cliente = serializers.IntegerField()
    id_empleado = serializers.IntegerField()

    def create(self, validated_data):
        return Pedido.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fecha_pedido = validated_data.get('fecha_pedido', instance.fecha_pedido)
        instance.fecha_envio = validated_data.get('fecha_envio', instance.fecha_envio)
        instance.id_cliente = validated_data.get('id_cliente', instance.id_cliente)
        instance.id_empleado = validated_data.get('id_empleado', instance.id_empleado)
        instance.save()
        return instance


###################
#  AREAS CLIENTE  #
###################

class AreaClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaCliente
        fields = ['id', 'no_empleados', 'id_area', 'id_cliente']

    id = serializers.IntegerField(read_only = True)
    no_empleados = serializers.IntegerField()
    id_area = serializers.IntegerField()
    id_cliente = serializers.IntegerField()

    def create(self, validated_data):
        return AreaCliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.no_empleados = validated_data.get('no_empleados', instance.no_empleados)
        instance.id_area = validated_data.get('id_area', instance.id_area)
        instance.id_cliente = validated_data.get('id_cliente', instance.id_cliente)
        instance.save()
        return instance


###############
#  PRODUCTOS  #
###############

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'producto', 'costo', 'precio', 'existencia', 'reorden', 'comprometidas', 'vigente', 'imagen']

    id = serializers.IntegerField(read_only = True)
    producto = serializers.CharField()
    costo = serializers.FloatField()
    precio = serializers.FloatField()
    existencia = serializers.IntegerField()
    reorden = serializers.IntegerField()
    comprometidas = serializers.IntegerField()
    vigente = serializers.BooleanField()
    imagen = serializers.CharField()

    def create(self, validated_data):
        return Producto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.producto = validated_data.get('producto', instance.producto)
        instance.costo = validated_data.get('costo', instance.costo)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.existencia = validated_data.get('existencia', instance.existencia)
        instance.reorden = validated_data.get('reorden', instance.reorden)
        instance.comprometidas = validated_data.get('comprometidas', instance.comprometidas)
        instance.vigente = validated_data.get('vigente', instance.vigente)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.save()
        return instance


#############################
#  PRODUCTOS AREAS CLIENTE  #
#############################

class ProductoAreaClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoAreaCliente
        fields = ['id', 'consumo', 'id_area_cliente', 'id_producto']
    
    id = serializers.IntegerField(read_only = True)
    consumo = serializers.IntegerField()
    id_area_cliente = serializers.IntegerField()
    id_producto = serializers.IntegerField()

    def create(self, validated_data):
        return ProductoAreaCliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.consumo = validated_data.get('consumo', instance.consumo)
        instance.id_area_cliente = validated_data.get('id_area_cliente', instance.id_area_cliente)
        instance.id_producto = validated_data.get('id_producto', instance.id_producto)
        instance.save()
        return instance


####################
#  DETALLE PEDIDO  #
####################

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['id', 'precio', 'descuento', 'cantidad', 'id_producto', 'id_pedido']

    id = serializers.IntegerField(read_only = True)
    precio = serializers.FloatField()
    descuento = serializers.FloatField()
    cantidad = serializers.FloatField()
    id_producto = serializers.IntegerField()
    id_pedido = serializers.IntegerField()

    def create(self, validated_data):
        return DetallePedido.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.precio = validated_data.get('precio', instance.precio)
        instance.descuento = validated_data.get('descuento', instance.descuento)
        instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        instance.id_producto = validated_data.get('id_producto', instance.id_producto)
        instance.id_pedido = validated_data.get('id_pedido', instance.id_pedido)
        instance.save()
        return instance