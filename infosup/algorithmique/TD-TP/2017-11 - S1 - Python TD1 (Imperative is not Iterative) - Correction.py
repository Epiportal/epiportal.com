#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:16:56 2017

@author: nathalie
"""

def max3(x, y, z):
    if y > x:
        x = y
    if z > x:
        x = z
    return x


"""
the day after
"""

# leap = bissextile
def leap(y):
    return (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))

def nbdays(m, y):
    """
    returns day number in month m of year y
    """
    if m == 2:
        if leap(y):
            return 29
        else:
            return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31

# another version
def nbDays(m, y):
    if m == 2:
        if leap(y):
            add = 1
        else:
            add = 0
        return 28 + add
    else:
        return (30 + (m - m//8) % 2)
    
def valid(d, m, y):
    """ 
    checks if the date (d, m, y) is valid
    """
    if m < 1 or m > 12:
        return False
    else:
        return (d >=1) and (d <= nbdays(m, y))

def valid2(d, m, y):
    return (m >= 1 and m <= 12) \
            and (d >= 1 and d <= nbdays(m, y))


def tomorrow(d, m, y):
    
    if not valid(d, m, y):
        raise Exception("date not valid")
    d = d + 1               # d = d % nbDays(m,y) + 1
    if d > nbdays(m, y):    # if  == 1:
        d = 1
        m = m + 1           # m = m % 12 + 1
        if m == 13:         # if m == 1:
            m = 1
            y = y+1

    return (d, m, y)


"""
list to 9
"""

def abs(x):
    if x < 0:
        return -x
    else:
        return x

def __list9(n):
    print(n, end=' ')
    if n < 10:
        print()
        return 1
    else:
        mir = (n % 10) * 10 + n // 10
        return 1 + __list9(abs(n - mir))
        
        

def list9(n):
    """
    displays the list to 9 list from n
    returns the number of elements
    """
    if n < 10 or n >= 100:
        raise Exception("not a 2-digit natural")
    
    nb = __list9(n)
    print(nb, "elements")
    
"""
Perfect number
"""

import math


def __sumdiv(n, d = 2):
    '''
    Displays proper divisors of n greater than d
    and returns their sum
    '''
    if d > math.sqrt(n):
        return 0
    else:
        if d * d == n:
            print(d, end=' ')
            return d
        elif n % d == 0:
            print(d, end=' ')
            res = d + n // d + __sumdiv(n, d + 1)
            print(n // d, end=' ')
            return res
        else:
            return __sumdiv(n, d + 1)


def perfect(n):
    if n < 2:
        raise Exception("n must be > 1")
    print(1, end=' ')
    if n == 1 + __sumdiv(n):
        print('\n', n, "is perfect")
    else:
        print('\n', n, "is not perfect")
        










       
        
        
        
        
        
        
        
        
