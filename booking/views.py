from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Booking
from .forms import NewBookingForm

class BookingView(LoginRequiredMixin, View):
    """
    This view pulls all the user bookings from the database and displays
    them on the my bookings page (accessible via profile page)
    """
    def get(self, request):
        bookings = Booking.objects.filter(email=request.user).order_by('-number')
        context = {
            "bookings" : bookings,
        }
        return render(request, 'booking/my_bookings.html', context)
    
    def get_object(self):
        return self.request.user

class NewBooking(LoginRequiredMixin, View):

    def get(self, request):
        booking_form = NewBookingForm(request.POST, instance=request.user)
        return render(request, 'booking/new_booking.html',
                      {'form': booking_form})
    
    def post(self, request):
        if request.method == 'POST':
            booking_form = NewBookingForm(data=request.POST,
                                          instance=request.user)
        if booking_form.is_valid():
            bookings = Booking.objects.filter(email=request.user).order_by('-number')
            number = len(bookings)+1
            first_name = self.request.user
            last_name = self.request.user
            email = self.request.user
            date = booking_form.cleaned_data['date']
            time = booking_form.cleaned_data['time']
            new_booking = Booking(number = number,
                                first_name = first_name,
                                last_name = last_name,
                                email = email,
                                date = date,
                                time = time,)
            new_booking.save()
            messages.add_message(request, messages.INFO,
                                 'Booking saved!')
            return redirect('user_bookings')
    
class DeleteBooking(LoginRequiredMixin, View):
    def get(self, request, pk):
        """Receive booking delete form"""
        booking = get_object_or_404(Booking, pk=pk)
        return render(
            request,
            'booking/delete_booking.html',
            {'booking': booking}
        )

    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        bookings = Booking.objects.filter(email=request.user).order_by('-number')
        booking.delete()
        messages.add_message(request, messages.INFO,
                                 'Booking deleted!')
        return render(request,
                      'booking/my_bookings.html',
                      {"bookings":bookings})