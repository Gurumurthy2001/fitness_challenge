from django import forms
from django.contrib.auth.models import User
from fitness_app.models import UserProfile, UserRegistrationForm


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserRegistrationForm
        fields = ['email', 'password', 'confirm_password']

    def save(self, commit=True):
        user_registration_form = super(UserRegistrationForm, self).save(commit=False)
        user = User.objects.create(email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            user_registration_form.user = user
            user_registration_form.save()
        return user_registration_form


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['DOB', 'gender', 'bio_line', 'picture', 'github_link', 'twitter_link', 'instagram_link']
        
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['bio_line'].required = False
    
        
class LoginForm(forms.Form):
  username = forms.CharField(max_length=65)
  password = forms.CharField(max_length=65, widget=forms.PasswordInput)
  
