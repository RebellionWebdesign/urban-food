from django.forms import ModelForm, DateInput, TimeInput
from .models import Booking

class NewBookingForm(ModelForm):
    """
    This class presents a booking form to the user. The fields like number,
    date_created and first_name/last_name are omitted because they are auto
    generated.
    """


    class Meta:
        model = Booking
        fields = ['date', 'time']
        widgets = {
            'date': DateInput(attrs={'class':'datepicker', 'type':'date'}),
            'time': TimeInput(attrs={'class':'timepicker', 'min':'12:00',
                                     'max':'23:00', 'type':'time'})
        }