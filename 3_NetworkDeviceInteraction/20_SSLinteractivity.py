# Python 3
# Communicate with TlS or SSL, returns webpage 

import ssl
import socket

#stream sock = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#instance of ssl wrapped socket
ssock = ssl.wrap_socket(s)

try:
	ssock.connect(("news.ycombinator.com", 443))
	print(ssock.cipher()) #print md5 or sha1 message digest and method used
except:
	print("error")

#write byte array out socket now that it is open
try:
	ssock.write(b"GET / HTTP/1.1 \r\n")
	ssock.write(b"Host: news.ycombinator.com\n\n")
except Exception as e:
	print("Write error: ", e)

# where you'll put data you read back in
data = bytearray()
try:
	data = ssock.read()
except Exception as e:
	print("read error: ", e)

# move from bytes to string of 8 bit characters to the terminal screen
print(data.decode("utf-8"))
