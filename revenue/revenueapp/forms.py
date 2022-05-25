from django.forms import ModelForm
from revenueapp.models import Venue, Review

class ReviewUpdateForm(ModelForm):
    """Form for updating a venue review."""
    class Meta:
        """Meta class for ReviewUpdateForm."""
        model = Review
        fields = '__all__'