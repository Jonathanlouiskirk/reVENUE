from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from revenueapp.views import HomeView, AboutView, VenueCreateView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, IndividualVenueView, UserCreateView, DevView


urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('venuecreate', VenueCreateView.as_view(), name='venue_create'),
    path('reviewcreate/<int:pk>', ReviewCreateView.as_view(), name='review_create'),

    path('individual_venue/<int:pk>', IndividualVenueView.as_view(), name='individual_venue'),

    path('reviewupdate/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
    path('reviewdelete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    # User Create Form
    path('usercreate', UserCreateView.as_view(), name='user_create'),
    path('dev', DevView.as_view(), name='dev'),

]
urlpatterns += staticfiles_urlpatterns()

"""
Django's built in login/logout urls and their URL names are:
accounts/login/ [name='login']
accounts/logout/ [name='logout']
"""