from django.forms import ModelForm
from revenueapp.models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReviewUpdateForm(ModelForm):
    """Form for updating a venue review."""
    class Meta:
        """Meta class for ReviewUpdateForm."""
        model = Review
        fields = '__all__'

class UserCreateForm(UserCreationForm):
    """Form for creating a new user."""
    class Meta:
        """Meta class for UserCreateForm."""
        model = User
        fields = ['username', 'password1', 'password2']