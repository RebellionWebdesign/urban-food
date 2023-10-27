from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Review)
class PostAdmin(admin.ModelAdmin):

    list_filter = ('author', 'rate', 'created_on')
    list_display = ['author', 'rate', 'created_on', 'last_modified']
    search_fields = ['author', 'rate']
    summernote_fields = ('content')
