from .views import BookingView, NewBooking, DeleteBooking
from django.urls import path

urlpatterns = [
    path('accounts/profile/bookings/', BookingView.as_view(), name='user_bookings'),
    path('accounts/profile/bookings/new_booking/', NewBooking.as_view(), name='new_booking'),
    path('accounts/profile/bookings/delete_booking/<int:pk>', DeleteBooking.as_view(), name='delete_booking'),
]