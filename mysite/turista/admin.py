from django.contrib import admin

# DEBIDO A QUE SOLO ES UNA TABLA QUE YA ESTA NORMALIZADA AL GENERAR EL FILEDSETS ME OCULTA TODA LA INFORMACION.
from .models import Info

class InfoAdmin(admin.ModelAdmin):

	#fieldsets = [
     #   ('Informacion General', {'fields': ['region','comuna','destino'], 'classes': ['collapse']}),
      #  ('Horarios',               {'fields': ['nombree'], 'classes': ['collapse']}),
       # ('Ubicacion',               {'fields': ['region','comuna', 'destino'], 'classes': ['collapse']}),
    #]
	list_display = ('nombree',) # lista que muestra
	list_filter = ('region',) # 
	search_fields = ('destino',) # campo de busqueda

admin.site.register(Info,InfoAdmin)