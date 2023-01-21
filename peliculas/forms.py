from django import forms
from .models import tablaPersona, tablaPelicula, tablaPremio, tablaCines

class formularioPersona(forms.ModelForm):
    class Meta:
        model = tablaPersona
        fields = '__all__'
        widgets = {'nacimiento': forms.DateInput( attrs={ 'type':'date' } ) }


class formularioPelicula(forms.ModelForm):
    class Meta:
        model = tablaPelicula
        fields = '__all__'


class formularioPremio(forms.ModelForm):
    class Meta:
        model = tablaPremio
        fields = '__all__'

class formularioCine(forms.ModelForm):
    class Meta:
        model = tablaCines
        fields = '__all__'