from django.contrib import admin

from .models import City, Street


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'timestamp')
    ordering = ['city', 'name']

# admin.site.register(City)
# admin.site.register(Street)
# Register your models here.
