from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, View
from .models import Review

class ReviewView(DetailView):

    def get(self, request):
        reviews = Review.objects.all()
        context = {
            "reviews" : reviews
        }
        return render(request, 'user/profile.html', context)

class UserProfileReview(LoginRequiredMixin, View):
    
    def get(self, request):
        user_reviews = Review.objects.all()
        context = {
            "user_reviews":user_reviews
        }
        return render(request, 'review/my_reviews.html', context)
