# forms.py
from django import forms
from django.contrib.auth.models import User
from fitness_app.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        fields = ['user','DOB','gender','address','bio_line', 'picture']
