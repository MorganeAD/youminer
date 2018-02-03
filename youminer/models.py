from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nbViewedVideos = models.IntegerField(default = 0)

class Category(models.Model):
    name = models.CharField(default = "", max_length = 255)

    def __str__(self):
        return self.name

class Author(models.Model):
    channelId    = models.CharField(default = "", max_length = 255, primary_key=True)
    channelTitle = models.CharField(default = "", max_length = 255)
    nbVideos     = models.CharField(default = "", max_length = 255)
    createdDate  = models.CharField(default = "", max_length = 255)
    url          = models.CharField(default = "", max_length = 255)
    thumbnail    = models.CharField(default = "", max_length = 255)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.channelTitle

class Video(models.Model):
    videoId      = models.CharField(default = "", max_length = 255, primary_key=True)
    author       = models.ForeignKey(Author, on_delete=models.CASCADE)
    title        = models.CharField(default = "", max_length = 255)
    image        = models.CharField(default = "", max_length = 255)
    created_date = models.CharField(default = "", max_length = 255)
    url          = models.CharField(default = "", max_length = 255)
    thumbnail    = models.CharField(default = "", max_length = 255)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
