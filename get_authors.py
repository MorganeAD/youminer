# -*- coding: latin-1 -*-

import json
import sys
import operator

channels = []
for i in range(0,int(sys.argv[1])):
    json_data = open(str(i) +".json")
    data = json.load(json_data)
    url = "https://www.youtube.com/user/"
    title = data['items'][0]['snippet']['title']
    nbVideo = data['items'][0]['statistics']['videoCount'] 
    channels.append((int(nbVideo), "	<li><a href=\"" + url + "\">" + title + " - nombre de videos : " + nbVideo + "</a></li>"))
    json_data.close()

channels.sort(key=lambda x: x[0])
for i in channels:
    print(i[1])
