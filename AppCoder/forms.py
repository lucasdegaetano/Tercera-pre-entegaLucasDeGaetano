from django import forms

class CategoriasFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField(max_length=40)
    categoria = forms.IntegerField()
    precio = forms.DecimalField(max_digits=6, decimal_places=2)
    stock = forms.IntegerField()