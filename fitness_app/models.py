from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userprofile')
    picture = models.ImageField(upload_to='profile_pic', default='default.jpg')
    DOB = models.DateField(auto_now=False,null=True, blank=True)
    gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6, default='male')
    bio_line = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} profile'
        
        
class UserRegistrationForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=32)
    confirm_password = models.CharField(max_length=32)

    def __str__(self):
        return self.user.username
