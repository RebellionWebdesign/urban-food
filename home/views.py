from django.shortcuts import render
from django.views import View
from review.models import Review
from user.models import User


class HomeView(View):
    """
    The home view. It aggregates data from review and user the displays it
    on the home page.
    """
    def get(self, request):
        reviews = Review.objects.all().order_by('-rate')
        users = User.objects.all()
        context = {
            "reviews" : reviews,
            "users" : users
        }
        return render(request, 'home/index.html', context)
