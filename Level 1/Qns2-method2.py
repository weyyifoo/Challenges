# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:19:45 2018

@author: Wey Yi
"""

#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320
#
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

import time

def factorial(n):
    k = 1
    for t in range(1,n+1):
        k = k * t

    return k

start = time.time()
print(factorial(1000000))
end = time.time()
timelapse = end - start

# regretfully method 2 isn't as fast as the recursive method