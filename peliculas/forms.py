from django import forms
from .models import tablaPersona

class formularioPersona(forms.ModelForm):
    class Meta:
        model = tablaPersona
        fields = '__all__'
        widgets = {'nacimiento': forms.DateInput( attrs={ 'type':'date' } ) }