from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


# Create your views here.
from apps.persona.forms import FormCuentaBancaria
from apps.persona.models import Persona, CuentaBancaria



@permission_required('persona.add_cuentabancaria')
def registrarCuentaBancariaPersona(request):
    if request.method == 'POST':
        formulario_cuenta = FormCuentaBancaria(request.POST, request.FILES)
        if formulario_cuenta.is_valid():
            #Crea instancia de persona
            nueva_instancia = formulario_cuenta.save()
            nueva_instancia.save()
            messages.success(request,
                             'Se ha asignado correctamente la cuenta bancaria')
            return redirect(reverse('home'))
    else:
        formulario_cuenta = FormCuentaBancaria()
    return render(request,'registrarCuentaBancaria.html',{'form':formulario_cuenta,
                                                          'persona': Persona.objects.all(),
                                                          })

@login_required
def mostrarListado(request):
    return render(request, 'listadoPersonasConCuenta.html', {'cuentas': CuentaBancaria.objects.all(),  # devulve el listado de todas las cuentas
                                                             })
