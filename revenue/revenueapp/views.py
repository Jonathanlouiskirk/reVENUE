"""Views module for revenueapp."""
# from unicodedata import name
from django.shortcuts import render,redirect
from django.views import View
# User model
from django.contrib.auth.models import User
# Django built-in edit views
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from revenueapp.models import Venue, Review
from revenueapp.forms import ReviewForm, UserCreateForm
# login required mixin
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(View):
    def get(self, request):
        
        venues = Venue.objects.all()
        context ={
            'venues' : venues
        }

     
        return render(
            request=request, template_name='home.html', context=context
            )

class AboutView(View):
    def get(self, request):
        return render(request=request, template_name='about.html')

# CreateView creates a form and passes to the template 'venue_form.html'
class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    fields = '__all__'
    success_url = reverse_lazy('home')
    
class ReviewCreateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        venue = Venue.objects.get(pk=pk)
        form = ReviewForm(initial={'venue': venue})
        return render(request, 'revenueapp/review_form.html', {'form': form, 'venue': venue})
    def post(self, request, pk):
        venue = Venue.objects.get(pk=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.venue = venue
            review.owner = request.user
            review.save()
            return redirect('individual_venue', pk=pk)
        return render(request, 'revenueapp/review_form.html', {'form': form})

class UserCreateView(FormView):
    template_name = 'user_create.html'
    form_class = UserCreateForm
    success_url = '/accounts/login/?next=/revenue/' 
    def form_valid(self, form):
        form.save()  # type: ignore
        return super().form_valid(form)
 
class IndividualVenueView(View):
    def get(self, request, pk):
        review_exist = Review.objects.filter(venue_id=pk).exists()
        venue = Venue.objects.get(id=pk)
        if review_exist:
            reviews = Review.objects.filter(venue_id=pk)
            return render(request=request, template_name='individual_venue.html',context={
                'review_exist':review_exist,
                'venue_id':pk,
                'venue':venue,
                'reviews':reviews,
                }
                )
       
        return render(request=request, template_name='individual_venue.html',context={
                'venue':venue
                }
                )

class ReviewUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        # get the review object where pk = pk
        review = Review.objects.get(id=pk)
        # create a form instance
        form = ReviewForm(instance=review)
        venue = Venue.objects.get(id=review.venue_id)
        context = {'form': form, 'venue': venue}
        return render(request, 'review_update_form.html', context)
    def post(self, request, pk):

        # Get the review object where venue id = pk
        old_review = Review.objects.get(id=pk)
        if 'Cancel' in request.POST:
            return redirect('individual_venue', pk=old_review.venue_id)
        # Instantiate the ModelForm with the POST data
        form = ReviewForm(request.POST, instance=old_review)
        # Save the new data
        form.save()
        return redirect('individual_venue', pk=old_review.venue_id)

class ReviewDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        # if this were a confirmation page it would
        # pass the review in to the template
        # display the review
        # and the template would display the delete form with method=post
        review = Review.objects.get(id=pk)
        context = {'review':review}
        # redirect to home
        return render(request, 'delete_confirmation.html', context=context)

    def post(self, request, pk):
        # Get the review where venue id = pk
        review = Review.objects.get(id=pk)
        if 'Cancel' in request.POST:
            return redirect('individual_venue', pk=review.venue_id)
        # Delete the review
        review.delete()
        return redirect('individual_venue', pk=review.venue_id)

# Landing page for developer convenience
class DevView(View):
    def get(self, request):
        return render(request, 'dev.html')