from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.
def clientes(request):
    losclientes = Cliente.objects.all()
    return render(request, 'gestionarClientes.html', {"misclientes": losclientes})

def registrarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    curp = request.POST["numcurp"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]

    guardarCliente = Cliente.objects.create(
        id_cliente = id_cliente,
        nombre = nombre,
        apellido = apellido,
        curp = curp,
        direccion = direccion,
        telefono = telefono,
        fecha_nacimiento = fecha_nacimiento
    ) 
    return redirect("clientes")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html", {"misclientes": cliente})

def editarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    curp = request.POST["numcurp"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.curp = curp
    cliente.direccion = direccion
    cliente.telefono = telefono
    cliente.fecha_nacimiento = fecha_nacimiento

    cliente.save()
    return redirect("clientes")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")
