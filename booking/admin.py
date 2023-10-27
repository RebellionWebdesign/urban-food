from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class PostAdmin(admin.ModelAdmin):

    list_filter = ('number', 'last_name', 'email')
    list_display = ['number', 'last_name', 'email', 'table', 'persons', 'date',
                    'time']
    search_fields = ['number', 'last_name', 'email', 'table', 'persons',
                     'date']
