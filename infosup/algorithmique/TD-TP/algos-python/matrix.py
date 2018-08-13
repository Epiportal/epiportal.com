# -*- coding: utf-8 -*-
"""
Matrices: classics
January 2016
@author: Nathalie
"""


#------------------------------------------------------------------------
# 1.1 Displays

def printmatrix(M):
    l = len(M)
    c = len(M[0])
    for i in range(l):
        for j in range(c):
            print(M[i][j], end=' ')
        print()
    
def prettyprint(M, d=0):
    l = len(M)
    c = len(M[0])
    if d == 0:
        for line in M:
            for e in line:
                d = max(d, len(str(e))) # triche....
    line = ""
    for i in range(c*(d+3)+1):
        line = line + '-'
    for i in range(l):
        print(line)
        for j in range(c):
            s = "| {:" + str(d) + "d}"
            print(s.format(M[i][j]), end=' ')
        print('|')
    print(line)

#------------------------------------------------------------------------
# 1.2 Init

def init(l, c, val):
    '''
    Init matrix full of "val"
    '''
    M = []
    for i in range(l):
        M.append([])
        for j in range(c):
            M[i].append(val)
    return M

import random

def build(l, c, vMax):
    '''
    Init random matrix: l x c, 
    with positive values up to vMax
    '''
    M = []
    for i in range(l):
        L = []
        for j in range(c):
            L.append(random.randint(0, vMax-1))
        M.append(L)
    return M

#--------------------------------------------------------------------
# load matrix from file

def __str2intlist(s):
    L = []
    (i, n) = (0, len(s))
    while i < n:
        word = ""
        while i < n and s[i] != ' ' and s[i] != '\n':
            word += s[i]
            i += 1
        L.append(int(word))
        i += 1
    return L

def loadMatrix(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    M = []
    for line in lines:
        M.append(__str2intlist(line))
    return M
        


