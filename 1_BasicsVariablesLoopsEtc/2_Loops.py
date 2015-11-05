#!/usr/bin/python

# 2_Loops.py
# Just forming a Python Code base in 3

name=input("What is your name? ")

#This is a top-check, you never get to 10
for i in range(1,10):
    print (name, i)

x=0
while True:
    print (x)
    x=x+1
    # You won't hit 15, you will break
    if (x==15):
        break

mylist=['one', 'two', 'three', 'four']
for i in mylist:
    print(i)

