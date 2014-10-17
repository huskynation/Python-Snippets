import json
import urllib
import urllib2

url = 'http://data.ny.gov/resource/d6yy-54nr.json'
data = urllib2.urlopen(url)
json_format = zip(json.load(data))

for x in json_format:
	print x
# print json_format
# js = json_format
# js

# url_get = urllib.urlopen(url)
# # url_read = list(url_get)
# url_read = url_get.readlines(url_get)
# url_split = url_read.splitline()
# print url_split
# print url_read
# print data
# datalist = list(data)
# json_format = json.load(data)
# js = json_format
# print datalist