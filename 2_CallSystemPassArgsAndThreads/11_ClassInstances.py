#!/usr/bin/python

# Python3

# Illustrating different instances of the
# same class

class classExample:
    def __init__(self, foo):
        self.myvar = foo

    def getval(self):
        return self.myvar

    def setval(self, y):
        self.myvar = y

ex1 = classExample("First Example")
ex2 = classExample("Second Example")
ex3 = classExample("Third Example")
x = ex1.getval()
print(x)
x = ex2.getval()
print(x)
x = ex3.getval()
print(x)
ex3.setval("Set a new value for the third example.")
x = ex3.getval()
print(x)

