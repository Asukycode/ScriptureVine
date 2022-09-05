from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
      pass

class Creator(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      
class Post(models.Model):
      author = models.ForeignKey(Creator, on_delete=models.CASCADE)
      #post_image = comming soon
      title = models.CharField(max_length=500)
      description = models.CharField(max_length=10000)
      time_posted = models.TimeField()

