from django.urls import path
from .views import HomeView,VenueView,VenueReviewView,IndividualVenueView,CreateVenueView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
   
    #Venue review
    path('venue_review/', VenueReviewView.as_view(),name='venue_review'),
    #Individual
    path('individual_venue/', IndividualVenueView.as_view(),name='individual_venue'),
    path('create_venue/',
    CreateVenueView.as_view(),name='create_venue')
]
