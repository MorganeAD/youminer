from django.shortcuts import render
from .models import Video
from .models import Category

def video_list(request, cat):
    videosCategory = Category.objects.get(name__iexact=cat)
    videos = Video.objects.filter(category=videosCategory.id)
    categories = Category.objects.all()
    return render(request, 'youminer/video_list.html', {'currentCat':cat, 'videos': videos, 'categories' : categories})

def video_list(request, cat):
    videosCategory = Category.objects.get(name__iexact=cat)
    videos = Video.objects.filter(category=videosCategory.id)
    categories = Category.objects.all()
    return render(request, 'youminer/video_list.html', {'currentCat':cat, 'videos': videos, 'categories' : categories})
