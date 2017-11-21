# -*- coding: latin-1 -*-

import json
json_data = open('data.json')
data = json.load(json_data)
json_data.close()
for i in range(len(data) - 1):
	url = "https://youtu.be/" + data['items'][i]['id']['videoId']
	title = data['items'][i]['snippet']['title']
	channel = data['items'][i]['snippet']['channelTitle']
	print("	<li><a href=\"" + url + "\">" + channel + " - " + title + "</a></li>")
