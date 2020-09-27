import urllib.request
import requests
import threading
import json

URL='https://api.thingspeak.com/channels/1160874/feeds.json?api_key=YOLQ8V4RT6JCZE8Q' # URL for the thingSpeak channel containing JSON file
numberOfResults = '&results=10' # Change the number at the end to change number of results extracted  

#parse  json file 
data = requests.get(URL + numberOfResults).json()

feed=[] # List where the extracted values of feed will be appeneded 

for x in data['feeds']:
    feed.append(x['field1'])

print('The last 10 CPU temperatures collected on the ThingSpeak channel:')
print(feed)
