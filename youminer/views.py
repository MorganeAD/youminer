from django.shortcuts import render
from .models import Video
from .models import Category
from .models import Author

import os
from django.contrib.auth import authenticate, login

def connected(request):
    username = request.user
    categories = Category.objects.all()
    return render(request, 'youminer/connected.html', {'username': username, 'categories' : categories})

def video_show(request, vId):
    video = Video.objects.get(videoId=vId, author__isnull=False)
    f = open('youminer/port','r')
    port = int(f.read())
    f = open('youminer/port','w')
    if port > 60010:
        f.write('60000')
    else:
        f.write(str(port+1))
    port = 8080

    # Run vlc in a fork
    newpid = os.fork()
    if newpid == 0:
        os.system('vlc --intf dummy --play-and-exit ' + video.url + ' :sout="#transcode{vcodec=theo,vb=800,scale=0.25,acodec=vorb,ab=128,channels=2,samplerate=44100}:http{mux=ogg,dst=:' + str(port) + '/}" :sout-keep')
        os._exit(0)

    categories = Category.objects.all()
    return render(request, 'youminer/video_show.html', {'video': video, 'port' : port, 'categories' : categories})

def video_list(request, cat):
    videosCategory = Category.objects.get(name__iexact=cat)
    videos = Video.objects.filter(category=videosCategory.id, author__isnull=False)
    categories = Category.objects.all()
    return render(request, 'youminer/video_list.html', {'videos': videos, 'categories' : categories})

def author_list(request, cat):
    authorsCategory = Category.objects.get(name__iexact=cat)
    authors = Author.objects.filter(category=authorsCategory.id)
    categories = Category.objects.all()
    return render(request, 'youminer/author_list.html', {'authors': authors, 'categories' : categories})
