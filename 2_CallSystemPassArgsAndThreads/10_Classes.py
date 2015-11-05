#!/usr/bin/python

# Python 3
# Data and methods in once place = class
# methods become



class classyClass:
    # Pass me my self, pass me in foo -- assign foo a variable
    # for my instance.
    def __init__(self, foo):
        self.myvar = foo

    # Need the getval method to access myvar
    def getval(self):
        return self.myvar

#set a variable equal to a class with a passed-in variable
classyClassInstanceVariable = classyClass("I'm the passed-in-value")

#get access to that method and store to variable x
x = classyClassInstanceVariable.getval()
print(x) + "\n"