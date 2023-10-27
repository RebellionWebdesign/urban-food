from django.contrib import admin
from .models import Table

@admin.register(Table)
class PostAdmin(admin.ModelAdmin):

    list_filter = ('number', 'persons', 'max_persons', 'booked_out')
    list_display = ['number', 'persons', 'max_persons', 'booked_out']
    search_fields = ['number', 'persons', 'max_persons', 'booked_out']
