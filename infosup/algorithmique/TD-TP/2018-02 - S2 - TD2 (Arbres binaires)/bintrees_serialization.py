# -*- coding: utf-8 -*-
"""
Binary Tree Serialization
February 2017
@author: Nathalie
"""

from algopy import bintree


"""
4.1 - Serialization
"""

def serialize(B, L):
    if B == None:
        L.append(None)
    else:
        L.append(B.key)
        serialize(B.left, L)
        serialize(B.right, L)

def serializeBinTree(B):
    L = []
    serialize(B, L)
    return L


#---------------------------------------------------
# from serialized form to tree

# the function returns the tree and the actual position in the string
    
def __buildTree(L, i=0):
    if i >= len(L) or L[i] == None:
        return (None, i+1)
    else:
        B = bintree.BinTree(L[i], None, None)
        i = i + 1
        (B.left, i) = __buildTree(L, i)        
        (B.right, i) = __buildTree(L, i)
        return (B, i)

def buildTreeFromSerial(L):
    (B, i) = __buildTree(L)
    return B
    
# last version: reverses the list, then use L.pop() => WARNING: list is lost
    
def __buildTreeS(L):
    if L == []:
        return None
    else:
        e = L.pop()
        if e == None:
            return None
        else:
            B = bintree.BinTree(e, None, None)
            B.left = __buildTreeS(L)    
            B.right = __buildTreeS(L)
            return B

def reverse(L):
    n = len(L)
    for i in range(n//2):
        (L[i], L[n-i-1]) = (L[n-i-1], L[i])
    return L

def buildTreeFromSerial2(L):
    return __buildTreeS(reverse(L))


