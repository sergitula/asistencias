from django.urls import path

from apps.persona.views import registrarCuentaBancariaPersona, mostrarListado

app_name = 'persona'
urlpatterns = [
    # programa views
    path('asignarCuentaBancaria/',registrarCuentaBancariaPersona, name='asignarCuentaBancaria'),
    path('listarCuentas/', mostrarListado , name='listarCuentas'),
]