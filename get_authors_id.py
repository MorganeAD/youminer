# -*- coding: latin-1 -*-

import json
json_data = open('videos.json')
data = json.load(json_data)
json_data.close()
ids = []
for i in range(len(data['items']) - 1):
    id = data['items'][i]['snippet']['channelId']
    if id not in ids:
        print(id)
        ids.append(id)
