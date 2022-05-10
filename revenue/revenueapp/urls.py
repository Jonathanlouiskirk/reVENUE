from django.urls import path
from .views import HomeView,VenueView,Venue_reviewView,Individual_VenueView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('', VenueView.as_view(), name='venue'),
    path('', Venue_reviewView.as_view()
    name='venue_review'),
    path('', Individual_Venue.as_view()
    name='individual_venue')
]
