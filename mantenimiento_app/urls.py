from django.urls import path
from mantenimiento_app import views

urlpatterns = [
    path("mantenimientos",views.mantenimientos,name="mantenimientos"),
    path("registrarMantenimiento/",views.registrarMantenimiento,name="registrarMantenimiento"),
    path("seleccionarMantenimiento/<id_mantenimiento>",views.seleccionarMantenimiento,name="seleccionarMantenimiento"),
    path("editarMantenimiento/",views.editarMantenimiento, name="editarMantenimiento"),
    path("borrarMantenimiento/<id_mantenimiento>",views.borrarMantenimiento,name="borrarMantenimiento"),
    
]