from django.forms import ModelForm
from review.models import Review

class NewReviewForm(ModelForm):
    """
    This form is used to create user reviews and ratings.
    """
    class Meta:
        model = Review
        fields = ['content', 'rate']

class EditReviewForm(ModelForm):
    """
    This form is used to edit user reviews and ratings.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class'] = 'form-content'
        self.fields['rate'].widget.attrs['class'] = 'rate'
    
    class Meta:
        model = Review
        fields = ['content', 'rate']