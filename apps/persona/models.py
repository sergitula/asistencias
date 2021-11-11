from django.db import models


class Persona(models.Model):
    GENERO_OPCIONES = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )
    dni = models.CharField(max_length=8, unique=True)
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=9, choices=GENERO_OPCIONES)
    domicilio = models.CharField(max_length=250)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre_completo',)

    def __str__(self):
        return '{}'.format(self.nombre_completo)


class EstadoSalud(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    es_discapacitado = models.BooleanField(null=True)
    posee_obesidad = models.BooleanField(null=True)
    posee_desnutricion = models.BooleanField(null=True)
    observaciones = models.TextField(blank=True)


# 1. Dentro de la app “persona”, generar el modelo “CuentaBancaria” con los datos que se muestran en el grafico anterior.
# Tener en cuenta las siguientes restricciones: 1.1. Creación del modelo. (0,5 puntos)
# 1.2. El atributo “banco_emisor” debe ser del tipo CharField, definiendo el atributo “choices”. (0,5 puntos)
# 1.3. El atributo “numero_cuenta” debe ser único para un mismo Banco Emisor. (0,5 puntos)
# 1.4. Los atributos “cbu” y “alias” deben ser únicos cada uno en forma independiente, en
# todo el sistema. (0,5 puntos)
#  1.5. El atributo “cbu” debe contener exactamente 22 dígitos numéricos. (0,5 puntos)
# 1.6. Una Cuenta Bancaria pertenece solo a una Persona, y una Persona puede tener una o ninguna Cuenta Bancaria.
# Modelar la relación que corresponda para este caso. (0,5 puntos)


class CuentaBancaria (models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

    GENERO_OPCIONES = (
        ('1', 'Banco central'),
        ('2', 'Banco Nacion'),
    )
    numero_cuenta = models.AutoField(primary_key=True, unique= True)
    cbu = models.CharField(unique=True, max_length=22)
    alias = models.CharField(unique=True, max_length=100)
    banco_emisor = models.CharField(max_length=1, choices= GENERO_OPCIONES)


