from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class PostQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active=True)


class PostModelManager(models.Manager):
    # calling custom queryset method from the manager
    # link: https://docs.djangoproject.com/en/4.1/topics/db/managers/

    def get_queryset(self):
        return PostQuerySet(
            self.model, using=self._db
        )

    def all(self):
        return self.get_queryset().active()
    # Note that self.get_queryset is kinda the same as Post.objects


class Post(models.Model):
    author = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, unique=True, )
    description = models.CharField(max_length=350, )
    body = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    objects = PostModelManager()

    def __str__(self):
        return f'{self.title} {self.author}'


    # def get_absolute_url(self):
    #     return rever


class Comment(models.Model):
    post = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name='comment')
    fullname = models.CharField(max_length=16)
    body = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.title} {self.fullname}"

