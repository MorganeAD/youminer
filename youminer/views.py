from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.filter()
    return render(request, 'youminer/video_list.html', {'videos': videos})
