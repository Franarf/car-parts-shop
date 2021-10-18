from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"   />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car image'

    list_display = ( 'id','thumbnail', 'title_car', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ( 'id','thumbnail', 'title_car') 
    list_editable = ('is_featured',)
    search_fields = ('id', 'title_car', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_filter = ('color', 'model', 'body_style', 'fuel_type')

admin.site.register(Car, CarAdmin)