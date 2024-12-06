from django.shortcuts import render, redirect
from .models import Mantenimiento
# Create your views here.
def mantenimientos(request):
    losmantenimientos = Mantenimiento.objects.all()
    return render(request, 'gestionarMantenimientos.html', {"mismantenimientos": losmantenimientos})

def registrarMantenimiento(request):
    id_mantenimiento = request.POST["txtid_mantenimiento"]
    fecha = request.POST["datefecha"]
    descripcion = request.POST["txtdescripcion"]
    costo = request.POST["numcosto"]
    id_vehiculo = request.POST["numid_vehiculo"]
    id_empleado = request.POST["numid_empleado"]
    tipo_mantenimiento = request.POST["txttipo_mantenimiento"]

    guardarMantenimiento = Mantenimiento.objects.create(
        id_mantenimiento = id_mantenimiento,
        fecha = fecha,
        descripcion = descripcion,
        costo = costo,
        id_vehiculo = id_vehiculo,
        id_empleado = id_empleado,
        tipo_mantenimiento = tipo_mantenimiento
    ) 
    return redirect("mantenimientos")

def seleccionarMantenimiento(request, id_mantenimiento):
    mantenimiento = Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
    return render(request, "editarMantenimientos.html", {"mismantenimientos": mantenimiento})

def editarMantenimiento(request):
    id_mantenimiento = request.POST["txtid_mantenimiento"]
    fecha = request.POST["datefecha"]
    descripcion = request.POST["txtdescripcion"]
    costo = request.POST["numcosto"]
    id_vehiculo = request.POST["numid_vehiculo"]
    id_empleado = request.POST["numid_empleado"]
    tipo_mantenimiento = request.POST["txttipo_mantenimiento"]
    mantenimiento = Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
    mantenimiento.fecha = fecha
    mantenimiento.descripcion = descripcion
    mantenimiento.costo = costo
    mantenimiento.id_vehiculo = id_vehiculo
    mantenimiento.id_empleado = id_empleado
    mantenimiento.tipo_mantenimiento = tipo_mantenimiento

    mantenimiento.save()
    return redirect("mantenimientos")

def borrarMantenimiento(request, id_mantenimiento):
    mantenimiento = Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
    mantenimiento.delete()
    return redirect("mantenimientos")
