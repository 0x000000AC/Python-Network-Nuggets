#!/usr/bin/python

# Python3
# Global variable example

# Add i outside of for loop to be a global variable
i = 0

for x in range(1,25):
    #  x is in scope
    i = x + i


print(x)

