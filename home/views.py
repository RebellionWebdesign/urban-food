from django.shortcuts import render
from django.views import View
from review.models import Review
from user.models import User


class HomeView(View):

    def get(self, request):
        reviews = Review.objects.all()
        users = User.objects.all()
        context = {
            "reviews" : reviews,
            "users" : users
        }
        return render(request, 'home/index.html', context)
