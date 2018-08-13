# -*- coding: utf-8 -*-
"""
Dec 2017
@author: Nathalie
"""

def newList(n, val):
    '''
    build a list with n values val
    '''
    L = []
    for i in range(n):
        L.append(val)
    return L
    
    
#------------------------------------------------------------------------------
# ex 2.1 histogram

def hist(s):
    '''
    returns the histogram of characters in s
    I.e., returns a list (an array) of length 256 giving the number
    of occurrences of each character.
    '''
    h = newList(256, 0)
    for c in s:
        h[ord(c)] += 1
    return h

def nb_char(s):
    h = hist(s)
    nb = 0
    for n in h:
        if n > 0:         # nb = nb + (n != 0)
            nb = nb + 1
    return nb
    
# most frequent character with an histogram
def frequent3(s):
    h = hist(s)
    m = 0
    for i in range(1, 255):
        if h[i] > h[m]:
            m = i
    return(h[m], chr(m))
    
#------------------------------------------------------------------------------
# ex 2.2 Eratosthenes
    
import math

def eratosthenes(n):
    prime = newList(n+1, True)
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    L = []
    for i in range(2, n+1):
        if prime[i]:
            L.append(i)
    return L
