from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, View
from .models import Review
from .forms import NewReviewForm, EditReviewForm

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
                messages.add_message(request, messages.INFO,
                                 'Review saved!')
        return redirect('user_reviews')
    
class DeleteReview(LoginRequiredMixin, View):
    def get(self, request, pk):
        """Receive review delete form"""
        review = get_object_or_404(Review, pk=pk)
        return render(
            request,
            'review/delete_review.html',
            {'review': review}
        )

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        messages.add_message(request, messages.INFO,
                                 'Review deleted!')
        return redirect('user_reviews')


class UpdateReview(LoginRequiredMixin, View):
    def get(self, request, pk):
        """Receive review update form"""
        update_form_content = Review.objects.get(pk=pk)
        update_form = EditReviewForm(data=request.POST, instance=request.user)
        review = get_object_or_404(Review, pk=pk)
        return render(
            request,
            'review/update_review.html',
            {'review': review,
             'update_form': update_form}
        )

    def post(self, request, pk):
        update_review = get_object_or_404(Review, pk=pk)
        update_form = EditReviewForm(data=request.POST, instance=update_review)
        if update_form.is_valid():
            update_review.save()
            messages.add_message(request, messages.INFO,
                                 'Review updated!')
        return redirect('user_reviews')
    