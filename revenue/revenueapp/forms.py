from django.forms import ModelForm
from revenueapp.models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReviewForm(ModelForm):
    """Form for updating a venue review."""
    class Meta:
        """Meta class for ReviewUpdateForm."""
        model = Review
        exclude = ['owner', 'venue']

class UserCreateForm(UserCreationForm):
    """Form for creating a new user."""
    class Meta:
        """Meta class for UserCreateForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']