from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class SignupForm(UserCreationForm):
    """
    This is the signup form which takes an email and a password.
    """
    class Meta:
        model = User
        fields = ("email",)


class ChangeForm(UserChangeForm):
    """
    This is the form which is used to change the mailadress.
    """
    class Meta:
        model = User
        fields = ("email",)


class ChangeUserForm(UserChangeForm):
    """
    This is the form which is used to change the user data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['password'].widget.attrs['class'] = 'hide'

    class Meta:
        model = User
        fields = ('image', 'username', 'first_name', 'last_name')
