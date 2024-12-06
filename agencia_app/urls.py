from django.urls import path
from agencia_app import views

urlpatterns = [

    path("",views.index,name="index"),
    path("agencias",views.agencias,name="agencias"),
    path("registrarAgencia/",views.registrarAgencia,name="registrarAgencia"),
    path("seleccionarAgencia/<id_agencia>",views.seleccionarAgencia,name="seleccionarAgencia"),
    path("editarAgencia/",views.editarAgencia, name="editarAgencia"),
    path("borrarAgencia/<id_agencia>",views.borrarAgencia,name="borrarAgencia"),
    
]