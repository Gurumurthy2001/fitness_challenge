from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
  title=models.CharField(max_length=255)
  description=models.TextField()
  duration=models.IntegerField()
  
  def __str__(self):
    return self.title
  

class UserProfile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  profile_pic= models.ImageField(upload_to='profile_pic/',blank=True,null=True)
  bio_line= models.TextField()
  
  def __str__(self):
    return self.user.username
  
  
  
class Activity(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  challenge=models.ForeignKey(Challenge,on_delete=models.CASCADE)
  date=models.DateField()
  
  def __str__(self):
    return f'{self.user.username} - {self.challenge.title}'
  