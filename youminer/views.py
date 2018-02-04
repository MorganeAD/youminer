from django.shortcuts import render, redirect
from .models import Video
from .models import Category
from .models import Author
from .models import CustomUser
from .models import Comment
from django.contrib.auth.models import User

import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout

from .forms import UserForm, CommentForm
from django.http import HttpResponseRedirect

from django.utils import timezone

def add_user(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            newCustomUser = CustomUser.objects.create(user=new_user)
            login(request, new_user)
            return render(request, 'youminer/connected.html', {'username': new_user.username, 'categories' : categories})
    else:
        form = UserForm() 
    return render(request, 'youminer/adduser.html', {'categories' : categories, 'form': form}) 

def connected(request):
    username = request.user
    categories = Category.objects.all()
    return render(request, 'youminer/connected.html', {'username': username, 'categories' : categories})

def profil(request):
    user = request.user
    print(user.customuser.nbViewedVideos)
    user = User.objects.get(username=user)
    categories = Category.objects.all()
    return render(request, 'youminer/profil.html', {'username': user.username, 'user': user, 'categories' : categories})

def logout_page(request, *args, **kwargs):
    username = request.user
    categories = Category.objects.all()
    logout(request, *args, **kwargs)
    return render(request, 'youminer/disconnected.html', {'username': username, 'categories' : categories})

def video_show(request, vId):       
    username = request.user
    if request.user.is_authenticated():
        customUser = CustomUser.objects.get(user=username)
        customUser.nbViewedVideos += 1
        customUser.save()
    video = Video.objects.get(videoId=vId, author__isnull=False)
    f = open('youminer/port','r')
    port = int(f.read())
    f = open('youminer/port','w')
    if port > 60010:
        f.write('60000')
    else:
        f.write(str(port+1))
    port = 8080

    comments = Comment.objects.filter(video=video)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = username
            comment.created_date = timezone.now()
            comment.video = video
            comment.save()
            #return redirect('video_show', pk=comment.pk )
    else:
        form = CommentForm()

    # Run vlc in a fork
    newpid = os.fork()
    if newpid == 0:
        os.system('vlc --intf dummy --play-and-exit ' + video.url + ' :sout="#transcode{vcodec=theo,vb=800,scale=0.25,acodec=vorb,ab=128,channels=2,samplerate=44100}:http{mux=ogg,dst=:' + str(port) + '/}" :sout-keep')
        os._exit(0)

    categories = Category.objects.all()
    return render(request, 'youminer/video_show.html', {'username': username, 'video': video, 'port' : port, 'categories' : categories, 'form': form, 'comments': comments})

def video_list(request, cat):
    username = request.user
    videosCategory = Category.objects.get(name__iexact=cat)
    videos = Video.objects.filter(category=videosCategory.id, author__isnull=False)
    categories = Category.objects.all()
    return render(request, 'youminer/video_list.html', {'username': username, 'videos': videos, 'categories' : categories})

def author_list(request, cat):
    username = request.user
    authorsCategory = Category.objects.get(name__iexact=cat)
    authors = Author.objects.filter(category=authorsCategory.id)
    categories = Category.objects.all()
    return render(request, 'youminer/author_list.html', {'username': username, 'authors': authors, 'categories' : categories, })

def comment_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=false)
            comment.author = "VAL"
            comment.created_date = timezone.now()
            comment.save()
            #return redirect('post_detail', pk=post.pk )
    else:
        form = CommentForm()
    return render(request, 'youminer/video_show.html', {'form': form})
