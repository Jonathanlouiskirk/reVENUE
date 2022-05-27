"""Views module for revenueapp."""
from unicodedata import name
from django.shortcuts import render,redirect
from django.views import View
# Django built-in edit views
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from revenueapp.models import Venue, Review
from revenueapp.forms import ReviewUpdateForm

class HomeView(View):
    def get(self, request):
        venue_ids=Review.objects.values_list('venue',flat=True)
        print(venue_ids)   
        venues = Venue.objects.filter(id__in=venue_ids)
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
 
class IndividualVenueView(View):
    def get(self, request,pk):
        review = Review.objects.get(venue_id=pk)
        seating=review.seating_rating
        sound=review.sound_rating
        scene=review.scene_rating
        bathrooms=review.bathrooms_rating
        overall=review.overall_rating
        comments=review.comments
        venue=Venue.objects.get(id=pk)
        return render(request=request, template_name='individual_venue.html',context={
            'seating':seating,
            'sound':sound,
            'scene':scene,
            'bathrooms':bathrooms,
            'overall':overall,
            'comments':comments,
            'venue_id':pk,
            'venue':venue

        
        }
        )

class ReviewUpdateView(View):
    def get(self, request, pk):
        # get the review object where venue id = pk
        review = Review.objects.get(venue_id=pk)
        # create a form instance
        form = ReviewUpdateForm(instance=review)
        # pass the form to the template
        context = {'form': form}
        return render(request, 'review_update_form.html', context)
    def post(self, request, pk):
        # if the Cancel button is clicked, redirect to individual venue page where venue id = pk
        # Right now there is no URL for this, so I'm redirecting to home
        if 'Cancel' in request.POST:
            return redirect('home')
        # Otherwise, the Save button is clicked so update the review
        # Get the review object where venue id = pk
        old_review = Review.objects.get(venue_id=pk)
        # Instantiate the ModelForm with the POST data
        form = ReviewUpdateForm(request.POST, instance=old_review)
        # Save the new data
        form.save()
        return redirect('home')

class ReviewDeleteView(View):
    def get(self, request, pk):
        # This Get method is for testing only, the 'delete' button will be a POST request.
        # Get the review where venue id = pk
        review = Review.objects.get(venue_id=pk)
        # Delete the review
        review.delete()
        # redirect to home
        return redirect('home')
    def post(self, request, pk):
        # Get the review where venue id = pk
        review = Review.objects.get(venue_id=pk)
        # Delete the review
        review.delete()
        # Redirect to home, for now. In the future, redirect to the venue page where venue id = pk
        return redirect('home')
