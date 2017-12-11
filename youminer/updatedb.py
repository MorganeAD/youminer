import os
import json
import csv
from youminer.models import Video
from youminer.models import Category
from youminer.models import Author

Video.objects.all().delete()	# suppression des resultats precedents
Category.objects.all().delete()

listeCategory = []				# recherche de la liste des categorie
fname = "youminer/cfg.csv"
file = open(fname)
try:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'q':
            i = 1
            while i < len(row):
                listeCategory.append(row[i])
                i+=1
finally:
    file.close()

#for keyword in ['big+data', 'realite+virtuelle', '3D']:
for keyword in listeCategory:
    os.system('sh youminer/ytinterface.sh ' + 'v ' + keyword)
    json_data = open('answer.json', 'rt', encoding='latin1')
    videosData = json.load(json_data)
    json_data.close()
    category = Category.objects.create(name=keyword.replace('+', ' '))

    channelIds = []
    for i in range(len(videosData['items']) - 1):
        channelId = videosData['items'][i]['snippet']['channelId']
        if channelId not in channelIds:
            channelIds.append(channelId)

    for i in range(0, len(channelIds)):
        os.system('sh youminer/ytinterface.sh ' + 'a ' + channelIds[i])
        json_data = open('answer.json', 'rt', encoding='latin1')
        authorsData = json.load(json_data)
        json_data.close()
        url = "https://www.youtube.com/user/"
        channelTitle = authorsData['items'][0]['snippet']['title']
        nbVideos = authorsData['items'][0]['statistics']['videoCount'] 
        createdDate = authorsData['items'][0]['snippet']['publishedAt']
        Author.objects.create(channelId=channelIds[i], channelTitle=channelTitle, url=url, nbVideos=nbVideos, createdDate=createdDate, category=category)

    for i in range(len(videosData['items']) - 1):
        videoId = videosData['items'][i]['id']['videoId']
        url = "https://youtu.be/" + videoId
        title = videosData['items'][i]['snippet']['title']
        channelId = videosData['items'][i]['snippet']['channelId']
        thumbnail = videosData['items'][i]['snippet']['thumbnails']['default']['url']
        author = Author.objects.get(channelId=channelId)
        Video.objects.create(videoId=videoId, author=author, title=title, url=url, thumbnail=thumbnail, category=category)
os.remove('answer.json')
