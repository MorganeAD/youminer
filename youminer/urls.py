from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^videos/(?P<cat>[\w ]+)/$', views.video_list, name='video_list'),
    url(r'^authors/(?P<cat>[\w ]+)/$', views.author_list, name='author_list'),
]
