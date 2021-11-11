from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import CuentaBancaria


class FormCuentaBancaria(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = ('persona','numero_cuenta','cbu', 'alias', 'banco_emisor')
