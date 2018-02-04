from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nbViewedVideos = models.IntegerField(default = 0)
    nbQuizz = models.IntegerField(default = 0)

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

class Comment(models.Model):
    video        = models.ForeignKey(Video, on_delete=models.CASCADE)
    author       = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.CharField(default = "", max_length = 255)
    content      = models.CharField(default = "", max_length = 255)
    
    def __str__(self):
        return self.content
from mongoengine import *
 
connect('quizz')

class QuestionModel(Document):
    _id      = IntField()
    question = StringField()
    answer   = IntField()
    choices  = ListField(StringField())
