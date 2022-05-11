from django.urls import path
from .views import HomeView,VenueView,VenueReviewView,IndividualVenueView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('', VenueView.as_view(), name='venue'),
    path('', VenueReviewView.as_view(),
    name='venuereview'),
    path('', IndividualVenueView.as_view()
    name='individualvenue')
]
