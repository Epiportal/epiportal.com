# -*- coding: utf-8 -*-
"""
Nov. 2017
@author: nathalie
"""

#------------------------------------------------------------------------------
# ex 1.1 q1
def count(x, L):
    cpt = 0
    for e in L:
        if e == x:         
            cpt = cpt + 1
    return cpt
    
# ex 1.1 q2
def isPresent(x, L):
    i = 0
    n = len(L)
    while (i < n) and (x != L[i]):
        i = i + 1
    return (i < n)

# with a sorted list, returns the position or -1 in case of a negative search
def search(x, L):
    i = 0
    n = len(L)
    while (i < n) and (x > L[i]):
        i = i + 1
    if i < n and L[i] == x:
        return i
    else:
        return -1

#------------------------------------------------------------------------------
# ex 1.2

def newList(n, val):
    '''
    build a list with n values val
    '''
    L = []
    for i in range(n):
        L.append(val)
    return L
    
#------------------------------------------------------------------------------
# ex 1.3 q1
    
def delete(L, k):
    if k < 0 or k >= len(L):
        raise Exception("k out of range")
    L2 = []
    for i in range(0, k-1):
        L2 = L2.append(L[i])
    for i in range(k-1, len(L)-1):
        L2 = L2.append(L[i])
    return L2


'''
delete: new version delete with "in place" modifications
'''

def delete2(L, k):
    if k < 0 or k >= len(L):
        raise Exception("k out of range")
    for i in range(k-1, len(L)-1):
        L[i] = L[i+1]
    L.pop()


# ex 1.3 q2
def insert(L, k, e):
    if k < 0 or k > len(L):
        raise Exception("k out of range")
    L2 = []
    for i in range(k):
        L2.append(L[i])
    L2.append(e)
    for i in range(k, len(L)):
        L2.append(L[i])
    return L2

'''
in place
''' 
def insert2(L, k, e):
    L.append(None)  # to add a "cell" at the end
    i = len(L)-1
    while i > k:
        L[i] = L[i-1]
        i = i - 1
    L[k] = e    
    
