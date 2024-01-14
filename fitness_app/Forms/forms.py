from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'date_of_birth']  # Add more fields as needed
