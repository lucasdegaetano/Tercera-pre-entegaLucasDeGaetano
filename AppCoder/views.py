from django.shortcuts import render
from AppCoder.models import Categorias,Productos,Clientes
from AppCoder.forms import CategoriasFormulario, ProductosFormulario,ClientesFormulario

# Create your views here.
def inicio(request):
    return render(request,'AppCoder/inicio.html')
def productos(request):
    return render(request,'AppCoder/productos.html')
def clientes(request):
    return render(request,'AppCoder/clientes.html')
def categorias(request):
    return render(request,'AppCoder/categorias.html')


def productosFormulario(request):
    return render(request, "AppCoder/productosFormulario.html")

"""
def clientesFormulario(request):
    
    if request.method == "POST":

        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        dni = request.POST.get("dni")
        email = request.POST.get("email")
        celular = request.POST.get("celular")

        clientes = Clientes(nombre = nombre,
                            apellido = apellido,
                            dni = dni,
                            email = email,
                            celular = celular)
        
        clientes.save()            

        return render(request, "AppCoder/inicio.html")        
        
    else:

        frmClientes = ClientesFormulario()
    
    return render(request, "AppCoder/productosFormulario.html", {"frmClientes":frmClientes})

"""

def clientesFormulario(request):       

    if request.method == "POST":

        frmClientes = ClientesFormulario(request.POST)

        if frmClientes.is_valid():

            data = frmClientes.cleaned_data

            nombre = data.get('nombre')
            apellido = data.get('apellido')
            dni = data.get('dni')
            email = data.get('email')
            celular = data.get('celular')

            clientes = Clientes(nombre = nombre,
                                apellido = apellido,
                                dni = dni,
                                email = email,
                                celular = celular)
            clientes.save()

            return render(request, "AppCoder/inicio.html")      

    else:

        frmClientes = ClientesFormulario()
    
    return render(request, "AppCoder/clientesFormulario.html", {"frmClientes":frmClientes})


def productosFormulario(request):       

    if request.method == "POST":

        frmProductos = ProductosFormulario(request.POST)

        if frmProductos.is_valid():

            data = frmProductos.cleaned_data

            nombre = data.get('nombre')
            categoria = data.get('categoria')
            precio = data.get('precio')
            stock = data.get('stock')

            productos = Productos(nombre = nombre,
                                  categoria = categoria,
                                  precio = precio,
                                  stock = stock)
            productos.save()

            return render(request, "AppCoder/inicio.html")      

    else:

        frmProductos = ProductosFormulario()
    
    return render(request, "AppCoder/productosFormulario.html", {"frmProductos":frmProductos})


def categoriasFormulario(request):       

    if request.method == "POST":

        frmCategorias = CategoriasFormulario(request.POST)

        if frmCategorias.is_valid():

            data = frmCategorias.cleaned_data

            categoria = Categorias(nombre=data['nombre'])
            categoria.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        frmCategorias = CategoriasFormulario()
    
    return render(request, "AppCoder/categoriasFormulario.html", {"frmCategorias":frmCategorias})
        

