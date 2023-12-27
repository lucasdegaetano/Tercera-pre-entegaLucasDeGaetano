from django import forms

class CategoriasFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)

class ProductosFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    categoria = forms.IntegerField()
    precio = forms.DecimalField(max_digits=6, decimal_places=2)
    stock = forms.IntegerField()    

class ClientesFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()
    celular = forms.IntegerField()