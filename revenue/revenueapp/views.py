from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request=request, template_name='home.html')
        
class VenueView(View):
    def get(self, request):
        return render(request=request, template_name='venue.html')

class Venue_reviewView(View):
    def get(self, request):
        return render(request=request, template_name='venue_review.html')       

class Individual_VenueView(View):
    def get(self, request):
        return render(request=request, template_name='individual_venue.html')       