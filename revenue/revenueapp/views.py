from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request=request, template_name='home.html')
        
class VenueView(View):
    def get(self, request):
        return render(request=request, template_name='venue.html')

class VenueReviewView(View):
    def get(self, request):
        return render(request=request, template_name='venuereview.html')       

class IndividualVenueView(View):
    def get(self, request):
        return render(request=request, template_name='individualvenue.html')       