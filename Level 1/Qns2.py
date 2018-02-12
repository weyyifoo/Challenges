# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:19:45 2018

@author: Wey Yi
"""

import time

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

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)
    
start = time.time()
print(factorial(1000))
end = time.time()
timelapse = end - start  