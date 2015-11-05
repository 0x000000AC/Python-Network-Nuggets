#!/usr/bin/python3

# Python3
# Calling the host OS functions through libraries
# Get your working directory, get your user id
# get environment variable

import os
#Only import call
from subprocess import call


print(os.getcwd())

# The value of the user id
print(os.getuid())
print("\n")
print(os.getenv("PATH"))

# System subroutine in OS library
os.system("ls -la")

# You can also enter the program and
# parameters this uses the call subroutine
# from the subprocess library instead of os
inp=input("Hit enter")
call(["netstat", "-an"])


