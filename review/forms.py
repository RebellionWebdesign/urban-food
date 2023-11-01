from django.forms import ModelForm
from review.models import Review

class NewReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rate']

class EditReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rate']