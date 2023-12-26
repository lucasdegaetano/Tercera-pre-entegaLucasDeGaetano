from django.shortcuts import render
from django.http import HttpResponse
from models import Categorias

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
def clientesFormulario(request):
    return render(request, "AppCoder/clientesFormulario.html")


def categoriasFormulario(request):
    
    if request.method == 'POST':

        frmCategorias = categoriasFormulario(request.POST)

        if frmCategorias.is_valid:

            data = frmCategorias.cleaned_data

            categoria= Categorias(  data['nombre'])
            categoria.save()

            return render(request, "AppCoder/inicio.html")
        
        else:

            frmCategorias = categoriasFormulario()
    
    return render(request, "AppCoder/categorias/Formulario.html", {"frmCategorias":frmCategorias})
        

