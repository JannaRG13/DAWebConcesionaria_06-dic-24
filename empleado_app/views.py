from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.
def empleados(request):
    losempleados = Empleado.objects.all()
    return render(request, 'gestionarEmpleados.html', {"misempleados": losempleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtid_empleado"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    curp = request.POST["numcurp"]
    cargo = request.POST["txtcargo"]
    sueldo = request.POST["numsueldo"]
    fecha_ingreso = request.POST["datefecha_ingreso"]

    guardarEmpleado = Empleado.objects.create(
        id_empleado = id_empleado,
        nombre = nombre,
        apellido = apellido,
        curp = curp,
        cargo = cargo,
        sueldo = sueldo,
        fecha_ingreso = fecha_ingreso
    ) 
    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleados.html", {"misempleados": empleado})

def editarEmpleado(request):
    id_empleado = request.POST["txtid_empleado"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    curp = request.POST["numcurp"]
    cargo = request.POST["txtcargo"]
    sueldo = request.POST["numsueldo"]
    fecha_ingreso = request.POST["datefecha_ingreso"]
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.curp = curp
    empleado.cargo = cargo
    empleado.sueldo = sueldo
    empleado.fecha_ingreso = fecha_ingreso

    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleados")
