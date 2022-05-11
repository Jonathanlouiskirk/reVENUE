from django.urls import path
from .views import HomeView, AboutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
]

urlpatterns += staticfiles_urlpatterns()