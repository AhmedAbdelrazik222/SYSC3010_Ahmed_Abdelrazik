import urllib.request
import requests

# fields to be imported 
EMAIL = 'AhmedAbdelrazik@cmail.carleton.ca'
GROUP = 'L2-M2'
IDENTIFIER = 'B'

# creating the URL
URL = 'https://api.thingspeak.com/update?api_key='
KEY = '54CDA6FJF4RCJ92C'
HEADER = '&field1={}&field2={}&field3={}'.format(EMAIL,GROUP,IDENTIFIER)
new_url = URL + KEY + HEADER

# uploading data
data  = urllib.requests.urlopen(new_url)