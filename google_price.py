import urllib
import re

url = urllib.urlopen('https://www.google.com/finance?q=aapl').read
regex = '<span id="ref_[^.]*_1">(.+?)</span>'

pattern = re.compile(regex)
results = re.findall(pattern,url)

print results

# https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c,&df=cpct&auto=1&ts=1412618933693&ei=dtoyVMDeH8jP8wb3mYCACw
