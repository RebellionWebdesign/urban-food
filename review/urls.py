from .views import UserProfileReview
from django.urls import path

urlpatterns = [
    path('', UserProfileReview.as_view(), name = 'user_reviews'),
]