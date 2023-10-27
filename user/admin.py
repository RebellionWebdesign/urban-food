from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import SignupForm, ChangeForm
from .models import User

@admin.register(User)
class CustomAdmin(UserAdmin):
    add_form = SignupForm
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

