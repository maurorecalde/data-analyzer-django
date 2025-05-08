from django import forms
from .models import ArchivoCSV

class ArchivoCSVForm(forms.ModelForm):
    class Meta:
        model = ArchivoCSV
        fields = ['nombre', 'archivo']
