"""Views module for revenueapp."""
from django.shortcuts import render
from django.views import View
# Django built-in edit views
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from revenueapp.models import Venue, Review


class HomeView(View):
    def get(self, request):
        return render(request=request, template_name='home.html')

class AboutView(View):
    def get(self, request):
        return render(request=request, template_name='about.html')

# CreateView creates a form and passes to the template 'venue_form.html'
class VenueCreateView(CreateView):
    model = Venue
    fields = '__all__'
    success_url = reverse_lazy('home')
    
# Testing foreignkey relationships in CreateView
class ReviewCreateView(CreateView):
    model = Review
    fields = '__all__'
    success_url = reverse_lazy('home')