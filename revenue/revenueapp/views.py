"""Views module for revenueapp."""
from unicodedata import name
from django.shortcuts import render
from django.views import View
# Django built-in edit views
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from revenueapp.models import Venue, Review
from revenueapp.forms import ReviewUpdateForm


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
class VenueCreateView(CreateView):
    model = Venue
    fields = '__all__'
    success_url = reverse_lazy('home')
    
# Testing foreignkey relationships in CreateView
class ReviewCreateView(CreateView):
    model = Review
    fields = '__all__'
    success_url = reverse_lazy('home')

class ReviewUpdateView(View):
    def get(self, request, pk):
        # get the review object where venue id = pk
        review = Review.objects.get(venue_id=pk)
        # create a form instance
        form = ReviewUpdateForm(instance=review)
        # pass the form to the template
        context = {'form': form}
        return render(request, 'review_update_form.html', context)