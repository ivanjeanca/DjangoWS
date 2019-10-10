# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-10 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AreaCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_empleados', models.IntegerField()),
                ('id_area', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('descuento', models.FloatField()),
                ('cantidad', models.FloatField()),
                ('id_producto', models.IntegerField()),
                ('id_pedido', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField()),
                ('fecha_envio', models.DateField()),
                ('id_cliente', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('costo', models.FloatField()),
                ('precio', models.FloatField()),
                ('existencia', models.IntegerField()),
                ('reorden', models.IntegerField()),
                ('comprometidas', models.IntegerField()),
                ('vigente', models.BooleanField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoAreaCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumo', models.IntegerField()),
                ('id_area_cliente', models.IntegerField()),
                ('id_producto', models.IntegerField()),
            ],
        ),
    ]
