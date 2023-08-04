from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.

# Clase personalizada para el modelo Laboratorio en el sitio administrativo
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Muestra las columnas 'id' y 'nombre' en la tabla
    ordering = ('id',)  # Ordena la tabla por el campo 'id'

# Clase personalizada para el modelo DirectorGeneral en el sitio administrativo
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')  # Muestra las columnas 'id', 'nombre' y 'laboratorio' en la tabla
    ordering = ('id',)  # Ordena la tabla por el campo 'id'

# Clase personalizada para el modelo Producto en el sitio administrativo
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    ordering = ('id',)  # Ordena la tabla por el campo 'id'

# Registra los modelos personalizados
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)