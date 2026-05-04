from django.db import models

class Inscripcion(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=25)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=11)
    foto = models.TextField(null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    referencia = models.CharField(max_length=12, unique=True)
    banco = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    cedula_documento = models.TextField(null=True, blank=True)
    comprobante_pago = models.TextField(null=True, blank=True)
    tipo_documento = models.CharField(max_length=1, default='V')
    contrasena = models.CharField(max_length=8, null=True, blank=True)
    fecha_pago = models.DateField(verbose_name='Fecha del Depósito', null=True, blank=True)

    # --- El único __str__ de Inscripción, con la identación correcta ---
    def __str__(self):
        return f"{self.cedula} - {self.nombres} {self.apellidos}"


class PagoMensualidad(models.Model):
    MESES = [
        (1, 'Mensualidad 1'),
        (2, 'Mensualidad 2'),
        (3, 'Mensualidad 3'),
    ]
    
    # Relación con el alumno
    alumno = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    mes_pagado = models.IntegerField(choices=MESES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    referencia = models.CharField(max_length=50)
    banco_emisor = models.CharField(max_length=50)
    fecha_pago = models.DateField()
    
    # Convertido a TextField para guardar el Base64 y que no se borre en Render
    comprobante = models.TextField(null=True, blank=True) 

    # --- El __str__ correcto para Pagos, usando self.alumno.cedula ---
    def __str__(self):
        return f"{self.alumno.cedula} - Mes {self.mes_pagado}"