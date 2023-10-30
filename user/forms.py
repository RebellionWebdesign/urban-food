from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class ChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)

class ChangeUserForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('image', 'username', 'first_name', 'last_name')