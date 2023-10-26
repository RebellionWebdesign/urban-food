from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreationForm, ChangeForm
from .models import User


class CustomAdmin(UserAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = User
    list_display = ("email","first_name", "last_name", "is_staff", "is_active",
                    "is_superuser")
    list_filter = ("last_name", "email", "is_staff", "is_active",)
    fieldsets = (
        ("Userdata", {"fields": ("image", "email", "first_name", "last_name",
                                 "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups",
                                    "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomAdmin)
