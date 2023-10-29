from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.shortcuts import render
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