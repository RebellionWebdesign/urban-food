from django.shortcuts import render
from django.views.generic import DetailView
from .models import Review

class ReviewView(DetailView):

    def get(self, request):
        reviews = Review.objects.all()
        context = {
            "reviews" : reviews
        }
        return render(request, 'user/profile.html', context)
