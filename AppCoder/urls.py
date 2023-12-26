from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name="inicio"),
    path('productos', views.productos, name="productos"),
    path('clientes', views.clientes, name="clientes"),
    path('categorias', views.categorias, name="categorias"),
    
    path('productosFormulario', views.productosFormulario, name="productosFormulario"),
    path('clientesFormulario', views.clientesFormulario, name="clientesFormulario"),
    path('categoriasFormulario', views.categoriasFormulario, name="categoriasFormulario"),


]