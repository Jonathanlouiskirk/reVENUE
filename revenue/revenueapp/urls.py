from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from revenueapp.views import HomeView, AboutView, VenueCreateView, ReviewCreateView,IndividualVenueView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('venuecreate', VenueCreateView.as_view(), name='venue_create'),
    path('reviewcreate', ReviewCreateView.as_view(), name='review_create'),
    path('individual_venue', IndividualVenueView.as_view(), name='individual_venue')
]
