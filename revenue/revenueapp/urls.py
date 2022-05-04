from django.urls import path
from .views import HomeView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
]