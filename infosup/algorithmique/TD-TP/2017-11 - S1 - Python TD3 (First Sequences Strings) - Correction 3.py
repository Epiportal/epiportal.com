# -*- coding: utf-8 -*-
"""
Dec. 2017

@author: Nathalie
"""
from random import randint
def buildAleaList(n, mval):
    L = []
    for i in range(n):
        L.append(randint(0,mval))
    return L
    

#------------------------------------------------------------------------------
"""
 selection sort
"""

def minimum(L, d = 0):
    '''
    d is an optionnal parameter
    needed for the selection sort
    '''
    pos = d
    for i in range(d+1, len(L)):
        if L[i] < L[pos]:
            pos = i
    return pos

# a nice version
def minimum2(L, d=0):
    f = len(L)-1
    while (d < f):
        if L[d] < L[f]:
            f = f-1
        else:
            d = d+1
    return d

# select sort, version in place
def selectSort(L):
    for i in range(len(L)-1):
        pos = minimum(L, i)
        (L[i], L[pos]) = (L[pos], L[i]) # swap
        

# In one function, minimum inlined

def selectSort2(L):
    n = len(L)
    for i in range(n-1):
        pos = i
        for j in range(i+1, n):
            if L[j] < L[pos]:
                pos = j
        (L[i], L[pos]) = (L[pos], L[i])
        
#------------------------------------------------------------------------------
"""
insertion sort
"""
        
#functions from first part: search (modified) and insert

#search modified
def search(x, L):
    '''
    returns the position where x is, or should be, in L
    '''
    i = 0
    n = len(L)
    while (i < n) and (x > L[i]):
        i = i + 1
    return i
    
def insert(L, k, e):
    L.append(None)
    i = len(L)-1
    while i > k:
        L[i] = L[i-1]
        i = i - 1
    L[k] = e        

def insertion(L, x):
    '''
    inserts x at its place in L sorted
    '''
    pos = search(x, L)  # can be changed to binary search!
    insert(L, pos, x)

# in one function
def insertion(x, L):
    n = len(L)
    # search position
    i = 0
    while (i < n) and (x > L[i]):
        i += 1
    # shifts
    L.append(None)
    for j in range(n, i, -1):
        L[j] = L[j-1]
    # insertion
    L[i] = x

def insertion2(x, L):
    '''
    search for place and shifts at the same time
    '''
    i = len(L) - 1
    L.append(None)
    while (i >= 0) and (x < L[i]):
        L[i+1] = L[i]
        i -= 1
    L[i+1] = x

# insertion sort

# first version: return a new list
def insertSort(L):
    R = []
    for x in L:
        insertion(x, R)
    return R


# In place : insertion2 inlined

def insertSort2(L):
    for i in range(len(L)):
        x = L[i]
        j = i - 1
        while j >= 0 and x < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = x


"""
bonus: bubble sort
"""

def bubbleSort(L):
    swap = True
    n = len(L)
    while swap:
        swap = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                (L[i], L[i+1]) = (L[i+1], L[i])
                swap = True
        n -= 1
