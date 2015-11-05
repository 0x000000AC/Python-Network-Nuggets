#!/usr/bin/python

# Python3
# Basic server.  Accepts 512 bytes if received and writes
# the information to the

import socket

# This will be number of bytes you expect to receive
size = 512

# Default to the local machine
host = ''

port = 5098

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Setting the socket to be able to be reusable
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#  Must bind socket to port
serverSocket.bind((host, port))

# Open 5 listeners so 5 connections can happen at once
serverSocket.listen(5)

#  accept from client address
client, addr = serverSocket.accept()
data = client.recv(size)

# if you actually get data from your client,
# open a writeable file
if data:
    myFile = open("received.dat", '+w')
    print("connection from: ", addr[0])
    myFile.write(addr[0])
    myFile.write(":")
    # Since you're getting a string of bytes, you want to get this out as
    # a character string to the file
    myFile.write(data.decode("utf-8"))
    myFile.close()
serverSocket.close()





