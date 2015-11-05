#!/usr/bin/python

# Python3

# Open file -> Write data (catch errors)
# To illustrate exceptions, you can chmod the file
# to where it is read only.

try:
    # File name is myfile, w stands for write, writes in the same directory as
    # execution.
    fhandle = open("myfile", "w")
    fhandle.write("I am text in the file.")
    print("Data Written")
except IOError as e:
    print("Exception caught: Unable to write to myfile ", e)
# If you don't know what kind of exception that it's going to be,
# you can catch all -- but obviously this isn't as helpful in troubleshooting
except Exception as e:
    print("Another error occurred ", e)
else:
    print("File written to successfully")
    fhandle.close()
