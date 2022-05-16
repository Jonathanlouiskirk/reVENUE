from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request=request, template_name='home.html')
        


class VenueReviewView(View):
    def get(self, request):
        return render(request=request, template_name='venue_review.html')       

class IndividualVenueView(View):
    def get(self, request):
        return render(request=request, template_name='individual_venue.html')       

class CreateVenueView(View):
    def get(self, request):
        return render(request=request, template_name='create_venue.html')       