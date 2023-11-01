from .views import UserProfileReview, NewReview, DeleteReview
from django.urls import path

urlpatterns = [
    path('', UserProfileReview.as_view(), name = 'user_reviews'),
    path('new_review/', NewReview.as_view(), name='new_review'),
    path('delete_review/<int:pk>', DeleteReview.as_view(), name='delete_review'),
]