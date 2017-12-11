from django.shortcuts import render
from .models import Video
from .models import Category
from .models import Author

def video_list(request, cat):
    videosCategory = Category.objects.get(name__iexact=cat)
    videos = Video.objects.filter(category=videosCategory.id)
    categories = Category.objects.all()
    return render(request, 'youminer/video_list.html', {'currentCat':cat, 'videos': videos, 'categories' : categories})

def author_list(request, cat):
    authorsCategory = Category.objects.get(name__iexact=cat)
    authors = Author.objects.filter(category=authorsCategory.id)
    categories = Category.objects.all()
    return render(request, 'youminer/author_list.html', {'currentCat':cat, 'authors': authors, 'categories' : categories})
