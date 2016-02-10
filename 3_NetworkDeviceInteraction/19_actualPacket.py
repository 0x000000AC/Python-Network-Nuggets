# Python 3
# You'll need administrative privileges to run as you
# dip into the kernel space to do something for you

from scapy.all import *

# for IP you can also set src where dst is
frame = Ether(dst="15:16:89:fa:dd:09")/IP(dst="127.0.0.1")/TCP()/"This is my payload"

print(frame)

sendp(frame)
