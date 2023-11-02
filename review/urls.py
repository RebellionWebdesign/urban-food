from .views import UserProfileReview, NewReview, DeleteReview, UpdateReview
from django.urls import path

urlpatterns = [
    path('account/profile/reviews/', UserProfileReview.as_view(),
         name = 'user_reviews'),
    path('account/profile/reviews/new_review/', NewReview.as_view(),
         name='new_review'),
    path('account/profile/reviews/delete_review/<int:pk>',
         DeleteReview.as_view(), name='delete_review'),
    path('account/profile/reviews/update_review/<int:pk>',
         UpdateReview.as_view(), name='update_review'),
]