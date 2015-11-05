#!/usr/bin/python

# Python3
# Used to Illustrate helper functions in Python

def sub(x,y):
    #  out of scope here
    z = x - y
    # just print, no return
    print(z)

# using parameters
def add(x,y):
    # return value from subroutine or function
    return x+y

# Use your helper functions
print(add(100,20))
sub(100,20)

