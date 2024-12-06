from django.urls import path
from venta_app import views

urlpatterns = [
    path("ventas",views.ventas,name="ventas"),
    path("registrarVenta/",views.registrarVenta,name="registrarVenta"),
    path("seleccionarVenta/<id_venta>",views.seleccionarVenta,name="seleccionarVenta"),
    path("editarVenta/",views.editarVenta, name="editarVenta"),
    path("borrarVenta/<id_venta>",views.borrarVenta,name="borrarVenta"),
    
]
