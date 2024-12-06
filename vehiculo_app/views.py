from django.shortcuts import render, redirect
from .models import Vehiculo
# Create your views here.
def vehiculos(request):
    losvehiculos = Vehiculo.objects.all()
    return render(request, 'gestionarVehiculos.html', {"misvehiculos": losvehiculos})

def registrarVehiculo(request):
    id_vehiculo = request.POST["txtid_vehiculo"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    anio = request.POST["numanio"]
    color = request.POST["txtcolor"]
    precio = request.POST["numprecio"]
    kilometraje = request.POST["numkilometraje"]

    guardarVehiculo = Vehiculo.objects.create(
        id_vehiculo = id_vehiculo,
        marca = marca,
        modelo = modelo,
        anio = anio,
        color = color,
        precio = precio,
        kilometraje = kilometraje
    ) 
    return redirect("vehiculos")

def seleccionarVehiculo(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id_vehiculo=id_vehiculo)
    return render(request, "editarVehiculos.html", {"misvehiculos": vehiculo})

def editarVehiculo(request):
    id_vehiculo = request.POST["txtid_vehiculo"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    anio = request.POST["numanio"]
    color = request.POST["txtcolor"]
    precio = request.POST["numprecio"]
    kilometraje = request.POST["numkilometraje"]
    vehiculo = Vehiculo.objects.get(id_vehiculo=id_vehiculo)
    vehiculo.marca = marca
    vehiculo.modelo = modelo
    vehiculo.anio = anio
    vehiculo.color = color
    vehiculo.precio = precio
    vehiculo.kilometraje = kilometraje

    vehiculo.save()
    return redirect("vehiculos")

def borrarVehiculo(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id_vehiculo=id_vehiculo)
    vehiculo.delete()
    return redirect("vehiculos")
