from django.contrib import admin

# Register your models here.

from hoteles.models import Hotel
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
   """Profile admin."""
   list_display = ('city')
   list_display_links = ('pk', 'hotel',)
   list_editable = ('city')

