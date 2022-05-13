from django.urls import path
from .views import HomeView,VenueView,VenueReviewView,IndividualVenueView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('venue/', VenueView.as_view(), name='venue'),
    path('venue_review/', VenueReviewView.as_view(),name='venue_review'),
    path('individual_venue/', IndividualVenueView.as_view(),name='individual_venue')
]
