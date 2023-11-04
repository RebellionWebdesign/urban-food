from django.forms import ModelForm
from review.models import Review

class NewReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rate']

class EditReviewForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class'] = 'form-content'
        self.fields['rate'].widget.attrs['class'] = 'rate'
    
    class Meta:
        model = Review
        fields = ['content', 'rate']