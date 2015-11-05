#!/usr/bin/python3

# Python3
# A simple program to illustrate breaking
# a task up into threads.  For this you need
# to have some OOP concepts like a class object
# in this case we have a thread object and it's attributes

import threading


class aThread(threading.Thread):
    # When you make an instance of the class, this will be run
    # to allocate space for that object's values.
    def __init__(self, num, val):
        threading.Thread.__init__(self)
        self.threadNum = num
        self.loopCount = val

    # Method to call myfunc and input that thread object's data
    def run(self):
        print("Starting run: ", self.threadNum)
        myfunc(self.threadNum, self.loopCount)


# The method that will be run constantly.  In each
# of the threads, you'll be taking in the passed value
# and multiplying it by that step until the


def myfunc(num, val):
    count = 0
    while count < val:
        print(num, " : ", val * count)
        count = count + 1


# Allocate a space in memory and throw in a value,
# then start the threads.  Each tx is an instance.
t1 = aThread(1, 15)
t2 = aThread(2, 20)
t3 = aThread(3, 25)
t4 = aThread(4, 30)

t1.start()
t2.start()
t3.start()
t4.start()

#  Group into an array of threads
#  so that you can walk through them


threads = []
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

#  Join each in the thread.  You will get more
#  interleaved output the higher the number of functions you have.
for t in threads:
    t.join()
