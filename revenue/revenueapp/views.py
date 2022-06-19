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
class VenueCreateView(CreateView):
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


# Testing User creation, returns user to dev page upon success
class UserCreateView(FormView):
    template_name = 'user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()  # type: ignore
        return super().form_valid(form)
 
class IndividualVenueView(View):
    def get(self, request,pk):
      
        review_exist = Review.objects.filter(venue_id=pk).exists()
        venue = Venue.objects.get(id=pk)
        name = venue.name
        address = venue.address
        city = venue.city
        state = venue.state
        website = venue.website
        image = venue.image

        if review_exist:
            review = Review.objects.get(venue_id=pk)
            seating=review.seating_rating
            sound=review.sound_rating
            scene=review.scene_rating
            bathrooms=review.bathrooms_rating
            overall=review.overall_rating
            comments=review.comments
            # venue=Venue.objects.get(id=pk)
            return render(request=request, template_name='individual_venue.html',context={
                'name': name,
                'address':address,
                'city':city,
                'state':state,
                'website':website,
                'image':image,
                'review_exist':review_exist,
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
       
        return render(request=request, template_name='individual_venue.html',context={
                'name':name,
                'address':address,
                'city':city,
                'state':state,
                'website':website,
                'image':image,
                'venue':venue
               

        }
                )
class ReviewUpdateView(View):
    def get(self, request, pk):
        # get the review object where pk = pk
        review = Review.objects.get(id=pk)
        # create a form instance
        form = ReviewForm(instance=review)
        venue = Venue.objects.get(review.venue_id)
        context = {'form': form, 'venue': venue}
        return render(request, 'review_update_form.html', context)
    def post(self, request, pk):
        # if the Cancel button is clicked, redirect to individual venue page where venue id = pk
        # Right now there is no URL for this, so I'm redirecting to home
        if 'Cancel' in request.POST:
            return redirect('home')
        # Otherwise, the Save button is clicked so update the review
        # Get the review object where venue id = pk
        old_review = Review.objects.get(id=pk)
        # Instantiate the ModelForm with the POST data
        form = ReviewForm(request.POST, instance=old_review)
        # Save the new data
        form.save()
        return redirect('home')

class ReviewDeleteView(View):
    def get(self, request, pk):
        # This Get method is for testing only, the 'delete' button will be a POST request.
        review = Review.objects.get(id=pk)
        # Delete the review
        review.delete()
        # redirect to home
        return redirect('individual_venue', pk=review.venue_id)

    def post(self, request, pk):
        # Get the review where venue id = pk
        review = Review.objects.get(id=pk)
        
        # Delete the review
        review.delete()
        # Redirect to home, for now. In the future, redirect to the venue page where venue id = pk
        return redirect('individual_venue', pk=review.venue_id)

# Landing page for developer convenience
class DevView(View):
    def get(self, request):
        return render(request, 'dev.html')