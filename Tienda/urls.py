"""Tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from API import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/empleados/', views.EmpleadoAPI),
    url(r'^api/empleados/<int:pk>/', views.EmpleadoAPI_ID),
    url(r'^api/clientes/', views.ClienteAPI),
    url(r'^api/clientes/<int:pk>/', views.ClienteAPI_ID),
    url(r'^api/areas/', views.AreaAPI),
    url(r'^api/areas/<int:pk>/', views.AreaAPI_ID),
    url(r'^api/pedidos/', views.PedidoAPI),
    url(r'^api/pedidos/<int:pk>/', views.PedidoAPI_ID),
    url(r'^api/areacliente/', views.AreaCliente),
    url(r'^api/areacliente/<int:pk>/', views.AreaCliente_ID),
    url(r'^api/productos/', views.ProductoAPI),
    url(r'^api/productos/<int:pk>/', views.ProductoAPI_ID),
    url(r'^api/productoareacliente/', views.ProductoAreaClienteAPI),
    url(r'^api/productoareacliente/<int:pk>/', views.ProductoAreaClienteAPI_ID),
    url(r'^api/detallepedido/', views.DetallePedidoAPI),
    url(r'^api/detallepedido/<int:pk>/', views.DetallePedidoAPI_ID),
]