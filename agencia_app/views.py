from django.shortcuts import render, redirect
from .models import Agencia
# Create your views here.
def index(request):
    return render(request, 'index.html')

def agencias(request):
    lasagencias = Agencia.objects.all()
    return render(request, 'gestionarAgencias.html', {"misagencias": lasagencias})

def registrarAgencia(request):
    id_agencia = request.POST["txtid_agencia"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    email = request.POST["txtemail"]
    sucursal = request.POST["txtsucursal"]
    horario = request.POST["txthorario"]

    guardarAgencia = Agencia.objects.create(
        id_agencia = id_agencia,
        nombre = nombre,
        direccion = direccion,
        telefono = telefono,
        email = email,
        sucursal = sucursal,
        horario = horario
    ) 
    return redirect("agencias")

def seleccionarAgencia(request, id_agencia):
    agencia = Agencia.objects.get(id_agencia=id_agencia)
    return render(request, "editarAgencias.html", {"misagencias": agencia})

def editarAgencia(request):
    id_agencia = request.POST["txtid_agencia"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    email = request.POST["txtemail"]
    sucursal = request.POST["txtsucursal"]
    horario = request.POST["txthorario"]
    agencia = Agencia.objects.get(id_agencia=id_agencia)
    agencia.nombre = nombre
    agencia.direccion = direccion
    agencia.telefono = telefono
    agencia.email = email
    agencia.sucursal = sucursal
    agencia.horario = horario

    agencia.save()
    return redirect("agencias")

def borrarAgencia(request, id_agencia):
    agencia = Agencia.objects.get(id_agencia=id_agencia)
    agencia.delete()
    return redirect("agencias")
