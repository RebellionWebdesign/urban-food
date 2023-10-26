from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meal

@admin.register(Meal)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('name', 'is_favourite')
    list_display = ['name']
    search_fields = ['name']
    summernote_fields = ('description')
