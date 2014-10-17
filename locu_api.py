import urllib2
import json


locu_api = 'eeb4fa3537ca43b72874c698ffad781f52f7b99e'
url = 'https://api.locu.com/v1_0/venue/search/?postal_code=02176&api_key=eeb4fa3537ca43b72874c698ffad781f52f7b99e'
json_obj = urllib2.urlopen('url')
data = json.load(json_obj)
print data
