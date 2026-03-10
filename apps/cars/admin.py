from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price_per_day', 'fuel_type', 'transmission', 'seats', 'availability')
    list_filter = ('brand', 'fuel_type', 'transmission', 'availability')
    search_fields = ('name', 'brand')
    readonly_fields = ('id',)
