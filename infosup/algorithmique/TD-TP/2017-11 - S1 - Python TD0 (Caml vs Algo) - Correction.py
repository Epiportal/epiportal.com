# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:46:52 2015

@author: Nathalie
"""

def test(n):
    return (n >= 100) and (n < 1000)

def abs(x):
    if x > 0:
        return x
    else:
        return -x
    
def digits(n):
    return (n // 100, (n // 10) % 10, n % 10)

def loop(n):
    if n >= 1000:
        return -1
    else:
        (a, b, c) = digits(n)
        if a + b + c == a * b * c:
            return n
        else:
            return loop(n+1)

# main

print("Give a 3-digit integer")
n = int(input())
n = abs(n)
if test(n):
    res = loop(n)
    if res == -1:
        print("No mystery number after", n)
    else:
        print(res, "is the mystery number")
else:
    print(n, "is invalid")
    
input() # to keep the window opened
