import os
import json
import csv
from youminer.models import Video

Video.objects.all().delete()	# suppression des resultats precedents

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
	os.system('sh youminer/ytinterface.sh ' + keyword)
	json_data = open('answer.json')
	data = json.load(json_data)
	json_data.close()
	for i in range(len(data['items']) - 1):
		url = "https://youtu.be/" + data['items'][i]['id']['videoId']
		title = data['items'][i]['snippet']['title']
		channel = data['items'][i]['snippet']['channelTitle']
		thumbnail = data['items'][i]['snippet']['thumbnails']['default']['url']
		category  = keyword
		Video.objects.create(channel=channel, title=title, url=url, thumbnail=thumbnail, category=keyword)
