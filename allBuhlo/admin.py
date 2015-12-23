from django.contrib import admin
from .models import Alcohol, Ingridient, IngLitr
from django.contrib.admin.widgets import FilteredSelectMultiple

# Register your models here.
class AlcoholAdmin(admin.ModelAdmin):
	filter_horizontal = ['ingredients',]
	

admin.site.register(Alcohol,AlcoholAdmin)
admin.site.register([Ingridient,IngLitr])