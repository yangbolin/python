# -*- coding: cp936 -*-
import urllib2,urllib,sys

url = "http://bolinyang.iteye.com/blog/1747045"

req = urllib2.Request(url)
for i in range(0, 50):
	fd = urllib2.urlopen(req)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data) 
print # print a blank line
