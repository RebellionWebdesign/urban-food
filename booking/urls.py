from .views import BookingView, NewBooking, DeleteBooking
from django.urls import path

urlpatterns = [
    path('account/bookings/', BookingView.as_view(), name='user_bookings'),
    path('account/bookings/new_booking/', NewBooking.as_view(), name='new_booking'),
    path('account/bookings/delete_booking/<int:pk>', DeleteBooking.as_view(), name='delete_booking'),
]