# -*- coding: utf-8 -*-
"""
S2 - 2018
Binary Trees: measures and traversals
"""

from algopy import bintree
from algopy import queue

def size(B):
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)

def height(B):
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))
    

def lce(B, prof = 0):
    if B == None:
        return (0, 0)
    else:
        if B.left == B.right:
            return (prof, 1)
        else:
            (lceLeft, nbleft) = lce(B.left, prof+1)
            (lceright, nbright) = lce(B.right, prof+1)
            return (lceLeft + lceright, nbleft + nbright)

def pme(B):
    if B == None:
        return 0
    else:
        (lc, nb) = lce(B)
        return lc / nb
        

def maxpath(B):
    """
    keys must be integers
    """
    if B == None:
        return 0
    else:
        return B.key + max(maxpath(B.left), maxpath(B.right))
                   

        
def dfs(B): #depth first search
    if B == None:
        print('_', end='')
    else:
        print('<', B.key, ',', end='')
        dfs(B.left)
        print(',', end='')
        dfs(B.right)
        print('>', end='')
        
        
        
def bfs(B): #breadth first search
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        while not q.isempty():
            B = q.dequeue()
            print(B.key, end= ' ')
            if B.left != None:
                q.enqueue(B.left)
            if B.right != None:
                q.enqueue(B.right)
                                  

def width(B):
    w_max = 0
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        w = 0
        while not q.isempty():
            B = q.dequeue()
            if B == None:
                w_max = max(w, w_max)
                if not q.isempty():
                    q.enqueue(None)  
                    w = 0
            else:
                w += 1
                if B.left != None:
                    q.enqueue(B.left)
                if B.right != None:
                    q.enqueue(B.right)
    return w_max

def width2(B): 
    w_max = 0
    if B != None:
        q = queue.Queue() #current
        q.enqueue(B)
        q2 = queue.Queue() #next level
        w = 0
        while not q.isempty():
            B = q.dequeue()
            (w, w_max) = (0, 0)
            if B.left != None:
                q2.enqueue(B.left)
            if B.right != None:
                q2.enqueue(B.right)
            if q.isempty():
                w_max = max(w, w_max)
                w = 0
                (q, q2) = (q2, q)
    return w_max