from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, View
from .models import Review
from .forms import NewReviewForm
from user.models import User

class ReviewView(DetailView):

    def get(self, request):
        reviews = Review.objects.all()
        context = {
            "reviews" : reviews
        }
        return render(request, 'user/profile.html', context)

class UserProfileReview(LoginRequiredMixin, DetailView):
    
    def get(self, request):
        reviews = Review.objects.filter(author=request.user).order_by('-created_on')
        context = {
            "reviews":reviews
        }
        return render(request, 'review/my_reviews.html', context)
    
    def get_object(self):
        return self.request.user

class NewReview(LoginRequiredMixin, View):

    def get(self, request):
        review_form = NewReviewForm(request.POST, instance=request.user)

        return render(request, 'review/new_review.html', {'form': review_form})
    
    def post(self, request):

        if request.method == 'POST':
            review_form = NewReviewForm(data=request.POST, instance=request.user)
            if review_form.is_valid():
                author = request.user
                review = review_form.cleaned_data['content']
                rate = review_form.cleaned_data['rate']
                new_review = Review(author = author,
                                    content = review,
                                    rate = rate)
                new_review.save()

        return redirect('user_reviews')
    
class DeleteReview(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'review/delete_review.html')
    
    def post(self, request):
        review = Review.objects.values_list('id', flat=True)

        if request.method == 'POST':
            review.delete()
            return redirect('user_reviews')
