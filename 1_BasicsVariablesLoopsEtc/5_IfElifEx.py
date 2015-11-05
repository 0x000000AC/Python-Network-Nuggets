#!/usr/bin/python

# Python3
# Take a value and see if it is
# different than another value

# Typecast string to int for the comparison
x = int(input("Enter a number "))

if (x < 1):
    print("Too small")
elif (x >= 1 and x <= 10):
    print("Goldilocks zone")
else:
    print("Too high")

