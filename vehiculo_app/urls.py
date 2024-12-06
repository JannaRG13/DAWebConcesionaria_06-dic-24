from django.urls import path
from vehiculo_app import views

urlpatterns = [
    path("vehiculos",views.vehiculos,name="vehiculos"),
    path("registrarVehiculo/",views.registrarVehiculo,name="registrarVehiculo"),
    path("seleccionarVehiculo/<id_vehiculo>",views.seleccionarVehiculo,name="seleccionarVehiculo"),
    path("editarVehiculo/",views.editarVehiculo, name="editarVehiculo"),
    path("borrarVehiculo/<id_vehiculo>",views.borrarVehiculo,name="borrarVehiculo"),
    
]