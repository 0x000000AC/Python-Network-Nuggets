#!/usr/bin/python

# Python3
# Simplest example of socket library
# and DNS resolution.

# Example output:
# 23.235.39.133
# ('google-public-dns-b.google.com', ['4.4.8.8.in-addr.arpa'], ['8.8.4.4'])

# Implementation of socket in Python is the old BSD implementation
import socket

#
print(socket.gethostbyname("0x000000ac.github.io"))

# Reverse lookup
print(socket.gethostbyaddr("8.8.4.4"))

