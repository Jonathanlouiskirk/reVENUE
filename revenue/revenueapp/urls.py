from django.urls import path
from .views import HomeView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()