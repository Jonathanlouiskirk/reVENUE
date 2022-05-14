from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from revenueapp.views import HomeView, AboutView, VenueCreateView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('venuecreate', VenueCreateView.as_view(), name='venue_create')
]

urlpatterns += staticfiles_urlpatterns()