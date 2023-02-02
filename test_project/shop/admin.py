from django.contrib import admin

from .models import Shop


@admin.register(Shop)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'street',
        'house',
        'timestamp',
        'to_open_time',
        'to_close_time',
    )
