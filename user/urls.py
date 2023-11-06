from .views import BaseView, UserProfile, DeleteUserView, ChangeUserView
from django.urls import path

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('accounts/profile/', UserProfile.as_view(),
         name='user_profile'),
    path('accounts/profile/edit/', ChangeUserView.as_view(),
         name='user_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(),
         name='user_delete'),
]
