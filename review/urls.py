from .views import UserProfileReview, NewReview
from django.urls import path

urlpatterns = [
    path('', UserProfileReview.as_view(), name = 'user_reviews'),
    path('new_review/', NewReview.as_view(), name='new_review')
]