from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from API import views

urlpatterns = [
    url(r'^api/empleados/$', views.EmpleadoList.as_view()),
    url(r'^api/empleados/(?P<pk>[0-9]+)/$', views.EmpleadoDetail.as_view()),
    url(r'^api/clientes/$', views.ClienteList.as_view()),
    url(r'^api/clientes/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view()),
    url(r'^api/areas/$', views.AreaList.as_view()),
    url(r'^api/areas/(?P<pk>[0-9]+)/$', views.AreaDetail.as_view()),
    url(r'^api/pedidos/$', views.PedidoList.as_view()),
    url(r'^api/pedidos/(?P<pk>[0-9]+)/$', views.PedidoDetail.as_view()),
    url(r'^api/areacliente/$', views.AreaClienteList.as_view()),
    url(r'^api/areacliente/(?P<pk>[0-9]+)/$', views.AreaClienteDetail.as_view()),
    url(r'^api/productos/$', views.ProductoList.as_view()),
    url(r'^api/productos/(?P<pk>[0-9]+)/$', views.ProductoDetail.as_view()),
    url(r'^api/productoareacliente/$', views.ProductoAreaClienteList.as_view()),
    url(r'^api/productoareacliente/(?P<pk>[0-9]+)/$', views.ProductoAreaClienteDetail.as_view()),
    url(r'^api/detallepedido/$', views.DetallePedidoList.as_view()),
    url(r'^api/detallepedido/(?P<pk>[0-9]+)/$', views.DetallePedidoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)