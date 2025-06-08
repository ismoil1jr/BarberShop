from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'booking_date', 'booking_time', 'number_of_people', 'created_at')
    list_filter = ('booking_date', 'created_at')
    search_fields = ('full_name', 'phone')