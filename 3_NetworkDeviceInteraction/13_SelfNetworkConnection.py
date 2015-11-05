#!/usr/bin/python

# A simple example of a network test to yourself
# You can listen with wireshark, netcat and others
# ex with netcat:  #nc -l 127.0.0.1 8534
# Then run the program #python3 13_SelfNetworkConnection.py

import socket

# No place like home 127.0.0.1
host = 'localhost'

# Call an instance of a socket AF_INET = of the Internet family
# SOCK_STREAM = TCP  SOCK_DGRAM = UDP
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tuple for connecting to host, port is randomly chosen by me
addr = (host,8534)

# Connect to yourself
mySocket.connect(addr)

# b in msg informs that it is a stream of bytes (an array of bytes)
# as opposed to a python string
try:
    msg = b"Sending Array of Bytes\n"
    mySocket.sendall(msg)
except socket.errno as e:
    print("Socket error ", e)
finally:
    mySocket.close()

