from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'title_car', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name','create_date')
    search_fields = ('first_name', 'last_name', 'email', 'title_car')
    list_per_page = 25


    
    # fieldsets = (
    #     ('Macchina', {
    #         'fields': ('car_id',)
    #     }),
    #     )
    
    
admin.site.register(Contact, ContactAdmin)