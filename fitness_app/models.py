from django.db import models
from django.contrib.auth.models import User
  
  
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  picture = models.ImageField(upload_to='profile_pic', default='default.jpg')
  DOB = models.DateField(null=True, blank=True)
  gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6, default='male')
  bio_line = models.TextField()
  address = models.TextField(null=True, blank=True)

  def __str__(self):
    return f'{self.user.username} profile'
  
  