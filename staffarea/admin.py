from django.contrib import admin
from .models import StaffArea

@admin.register(StaffArea)
class PostAdmin(admin.ModelAdmin):

    list_filter = ('booking_number', 'last_name', 'email', 'booking_date')
    list_display = ['booking_number', 'last_name', 'email', 'table', 'persons',
                    'booking_date', 'booking_time']
    search_fields = ['booking_number', 'last_name', 'email', 'table', 'persons',
                     'booking_date']
