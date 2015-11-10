#!/usr/bin/python

# Python 2
# Simply prints of the packet numbers until you 
# kill it.  Tested successfully on xubuntu and OSX El Capitan
# A note on El Capitan: you need to install pcapy, easiest way is pip
# However, I had to disable El Capitan's new System Integrity protection
# to install via pip first.

# An implementation in Python of pcap library, might have to
# install via pip (or whatever installer you wish).
import pcapy

# Get all your network devices
devs = pcapy.findalldevs()
print(devs)

# Device, # of byte to capture per packet, promiscuous mode, timeout (ms)
# 65536 is the maximum size for TCP or UDP.
# Need Admin to run in promiscuous mode.
# You could skip this altogether on OSX with:
# sudo airport en1 sniff 1  and parse the pcap file 
cap = pcapy.open_live("en1", 65536 , 1 , 0)

# Not going to do anything yet.  Infinite loop, will always bave a count
count = 1
while count:
	# Next is the next packet in the stream
    (header, payload) = cap.next()
    print(count)
    count = count + 1
