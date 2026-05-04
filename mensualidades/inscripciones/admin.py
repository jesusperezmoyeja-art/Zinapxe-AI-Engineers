from django.contrib import admin
from django.utils.html import format_html
from .models import Inscripcion, PagoMensualidad

# Esta pequeña función revisa y repara el código Base64 si le falta el prefijo
def reparar_base64(texto):
    if not texto:
        return None
    # Si el texto ya tiene el prefijo, lo dejamos igual
    if texto.startswith('data:image'):
        return texto
    # Si le falta el prefijo, se lo agregamos automáticamente
    return f"data:image/jpeg;base64,{texto}"

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombres', 'apellidos', 'ver_comprobante_inscripcion')
    readonly_fields = ('ver_foto_grande',)

    def ver_comprobante_inscripcion(self, obj):
        src = reparar_base64(obj.comprobante_pago)
        if src:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px; object-fit: cover;" />', src)
        return "Sin comprobante"
    ver_comprobante_inscripcion.short_description = 'Capture Inscripción'

    def ver_foto_grande(self, obj):
        src = reparar_base64(obj.comprobante_pago)
        if src:
            return format_html('<img src="{}" style="max-width: 400px; max-height: 400px; border: 2px solid #ccc;" />', src)
        return "No hay imagen"
    ver_foto_grande.short_description = 'Comprobante de Inscripción (Grande)'


class PagoMensualidadAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'mes_pagado', 'fecha_pago', 'monto', 'ver_comprobante_mensual')
    readonly_fields = ('ver_foto_grande_mensual',)
    list_filter = ('mes_pagado',) 

    def ver_comprobante_mensual(self, obj):
        src = reparar_base64(obj.comprobante)
        if src:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px; object-fit: cover;" />', src)
        return "Sin comprobante"
    ver_comprobante_mensual.short_description = 'Capture Mensualidad'

    def ver_foto_grande_mensual(self, obj):
        src = reparar_base64(obj.comprobante)
        if src:
            return format_html('<img src="{}" style="max-width: 400px; max-height: 400px; border: 2px solid #ccc;" />', src)
        return "No hay imagen"
    ver_foto_grande_mensual.short_description = 'Comprobante de Mensualidad (Grande)'

# Registramos los modelos
admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(PagoMensualidad, PagoMensualidadAdmin)