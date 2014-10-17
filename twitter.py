import json
import urllib
import urllib2

url = 'https://api.twitter.com/1.1/search/tweets.json?q=isis'
data = urllib.urlopen(url)
json_format = json.load(data)
print json_format
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
