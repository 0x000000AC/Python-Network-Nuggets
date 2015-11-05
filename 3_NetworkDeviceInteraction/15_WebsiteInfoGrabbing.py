#!/usr/bin/python

# Python 3
# Connects out to a website in order to
# pull information presented by the site.
# Can be done with http libraries, but this is
# the most simple case.

import socket
# For regular expressions
import re

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(("news.ycombinator.com", 80))

# Get message to pull information from the website
http_get = b"GET / HTTP/1.1\nHost: news.ycombinator.com\n\n"
data = ''

# Send the byte get request.
try:
    mySocket.sendall(http_get)
    data = mySocket.recvfrom(1024)
except mySocket.error:
    print ("Socket error", mySocket.errno)
finally:
    print("Closing connection to the site")
    print("\n")
    mySocket.close()

# Convert the byte data you have to a string
rcvdData = data[0].decode("utf-8")

# Looks like one long line so split it at newline into multiple strings
individualLines = rcvdData
print(individualLines + "\n")
# Split that info by line into an array that contains each line
individualLines = rcvdData.splitlines()
print(individualLines)

# Iterate over the array and find the server type, then pull it out
# to display.
for s in individualLines:
    if re.search('Server:', s):
        s = s.replace("Server: ", "")
        print(s)
