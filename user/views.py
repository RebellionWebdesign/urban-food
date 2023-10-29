from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView, View
from django.shortcuts import render, redirect
from .models import User

class BaseView(DetailView):

    def get(self, request):
        return render(request, 'base.html')

class UserProfile(LoginRequiredMixin, DetailView):
    template_name = 'user/profile.html'
    context_object_name = 'user_profile'

    def get(self, request):
        users = User.objects.all()
        context = {
            "users" : users,
        }

        return render(request, 'user/profile.html', context)
    
    def get_object(self, *args, **kwargs):
        return self.request.user

class DeleteUserView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'user/delete_user.html')
    
    def post(self, request):
        user = self.request.user

        if request.method == 'POST':
            user.delete()
            messages.success(request, 'User deleted!')

            return redirect('home')
