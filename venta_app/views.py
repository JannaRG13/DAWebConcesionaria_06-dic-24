
from django.shortcuts import render, redirect
from .models import Venta
# Create your views here.
def ventas(request):
    lasventas = Venta.objects.all()
    return render(request, 'gestionarVentas.html', {"misventas": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtid_venta"]
    fecha = request.POST["datefecha"]
    precio = request.POST["numprecio"]
    forma_pago = request.POST["txtforma_pago"]
    id_vehiculo = request.POST["numid_vehiculo"]
    id_cliente = request.POST["numid_cliente"]
    id_empleado = request.POST["numid_empleado"]

    guardarVenta = Venta.objects.create(
        id_venta = id_venta,
        fecha = fecha,
        precio = precio,
        forma_pago = forma_pago,
        id_vehiculo = id_vehiculo,
        id_cliente = id_cliente,
        id_empleado = id_empleado
    ) 
    return redirect("ventas")

def seleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    return render(request, "editarVentas.html", {"misventas": venta})

def editarVenta(request):
    id_venta = request.POST["txtid_venta"]
    fecha = request.POST["datefecha"]
    precio = request.POST["numprecio"]
    forma_pago = request.POST["txtforma_pago"]
    id_vehiculo = request.POST["numid_vehiculo"]
    id_cliente = request.POST["numid_cliente"]
    id_empleado = request.POST["numid_empleado"]
    venta = Venta.objects.get(id_venta=id_venta)
    venta.fecha = fecha
    venta.precio = precio
    venta.forma_pago = forma_pago
    venta.id_vehiculo = id_vehiculo
    venta.id_cliente = id_cliente
    venta.id_empleado = id_empleado

    venta.save()
    return redirect("ventas")

def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("ventas")
