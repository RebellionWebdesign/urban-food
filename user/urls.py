from .views import BaseView, UserProfile, DeleteUserView
from django.urls import path

urlpatterns = [
    path('', BaseView.as_view(), name = 'home'),
    path('accounts/profile/', UserProfile.as_view(), name='user_profile'),
    path('accounts/profile/delete/', DeleteUserView.as_view(),
         name='user_delete')
]