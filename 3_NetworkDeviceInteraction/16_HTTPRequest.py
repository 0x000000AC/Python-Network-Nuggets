#!/usr/bin/python

# Python3
# Ex output:
# 301
# Date: Mon, 02 Nov 2015 04:24:36 GMT
# Content-Type: text/html
# Content-Length: 178
# Connection: keep-alive
# Set-Cookie: __cfduid=d6a26b48b8b696327db506fb41f36aba51446438276; expires=Tue, 01-Nov-16 04:24:36 GMT; path=/; domain=.ycombinator.com; HttpOnly
# Location: https://news.ycombinator.com/
# Server: cloudflare-nginx
# CF-RAY: 23ed121bc731244a-IAD

# There are a number of libraries that will do this besides
# http
import http.client

hst = http.client.HTTPConnection("news.ycombinator.com")

# / indicates top level directory
hst.request("GET", "/")
data = hst.getresponse()

# Status from the server
print (data.code)

print (data.headers)
text = data.readlines()
for t in text:
    print(t.decode('utf-8'))

