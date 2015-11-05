#!/usr/bin/python

# Python3
# argparse allows you to quickly/easily take user input
# from the command line to be used for flags etc in a program
# In this case, you'll simply be getting back the string that
# you pass in.
# ex:  #python3 8_ArgPassing.py -i Hello
#      hello

import argparse

# Create parser object.
parser = argparse.ArgumentParser(description="This is our description")

# -i is the argument you expect.   It is required.   Help will be what you need.
parser.add_argument('-i', type=str, help="This is the help you get to describe the parameter", required=True)
parser.add_argument('-o', type=str, help="This is optional", required=False)

#  Part of a dictionary/hash
cmdargs = parser.parse_args()

#  The '-i' flag creates a variable i in the parser object
ivar = cmdargs.i
print(ivar)
