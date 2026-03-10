from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('car', 'customer_name', 'email', 'pickup_date', 'return_date', 'total_price', 'status')
    list_filter = ('status', 'pickup_date', 'return_date')
    search_fields = ('customer_name', 'email', 'car__name')
    readonly_fields = ('created_at',)
