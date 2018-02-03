from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^videos/(?P<cat>[\w ]+)/$', views.video_list, name='video_list'),
    url(r'^video/(?P<vId>[\w ]+)/$', views.video_show, name='video_show'),
    url(r'^authors/(?P<cat>[\w ]+)/$', views.author_list, name='author_list'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='youminer/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='youminer/disconnected.html'), name='logout'),
    url(r'^connected/$', views.connected, name='connected'),
]
