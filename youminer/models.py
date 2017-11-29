from django.db import models
from django.utils import timezone


class Video(models.Model):
    channel      = models.CharField(default = "", max_length = 255)
    title        = models.CharField(default = "", max_length = 255)
    image        = models.CharField(default = "", max_length = 255)
    created_date = models.CharField(default = "", max_length = 255)
    url          = models.CharField(default = "", max_length = 255)
    thumbnail    = models.CharField(default = "", max_length = 255)
    category     = models.CharField(default = "", max_length = 255)

    def __str__(self):
        return self.channel + " - " + self.title

class Author(models.Model):
    channelId    = ""
    channelTitle = ""
    nbVideos     = ""
    created_date = ""

    def __str__(self):
        return self.channelTitle
