from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    author = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, unique=True,)
    description = models.CharField(max_length=350,)
    body = models.TextField()
    comment = models.ForeignKey("Comment",on_delete=models.CASCADE, related_name='comment')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    pass
