from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView, View
from django.shortcuts import render, redirect
from .forms import ChangeUserForm
from .models import User


class BaseView(DetailView):
    """
    This view displays the user images on the reviews section.
    """

    def get(self, request):
        return render(request, 'base.html')


class UserProfile(LoginRequiredMixin, DetailView):
    """
    This view displays the user profile.
    """
    template_name = 'user/profile.html'
    context_object_name = 'user_profile'

    def get(self, request):
        users = User.objects.all()
        context = {
            "users": users,
        }

        return render(request, 'user/profile.html', context)

    def get_object(self):
        return self.request.user


class DeleteUserView(LoginRequiredMixin, View):
    """
    This view displays deletes the user profile.
    """

    def get(self, request):
        return render(request, 'user/delete_user.html')

    def post(self, request):
        user = self.request.user

        if request.method == 'POST':
            user.delete()
            messages.success(request, 'User deleted!')

            return redirect('home')


class ChangeUserView(LoginRequiredMixin, View):
    """
    This view displays is used to change user info.
    """

    def get(self, request):
        change_form = ChangeUserForm(instance=request.user)

        return render(request, 'user/change_user.html',
                      {'change_form': change_form})

    def post(self, request):
        change_form = ChangeUserForm(request.POST, instance=request.user)

        if request.method == 'POST':
            if change_form.is_valid():
                change_form.save()
                messages.add_message(request, messages.INFO,
                                     'Profile was changed!')
                return redirect('user_profile')
