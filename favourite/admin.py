from django.contrib import admin
from .models import Favourite

@admin.register(Favourite)
class PostAdmin(admin.ModelAdmin):

    list_filter = ('username', 'name')
    list_display = ['name', 'username', 'favourite']
    search_fields = ['name', 'username', 'favourite']
