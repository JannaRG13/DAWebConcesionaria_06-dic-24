from django.urls import path
from cliente_app import views

urlpatterns = [
    path("clientes",views.clientes,name="clientes"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<id_cliente>",views.seleccionarCliente,name="seleccionarCliente"),
    path("editarCliente/",views.editarCliente, name="editarCliente"),
    path("borrarCliente/<id_cliente>",views.borrarCliente,name="borrarCliente"),
    
]