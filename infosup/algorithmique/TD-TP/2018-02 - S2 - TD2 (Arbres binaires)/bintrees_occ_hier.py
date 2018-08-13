# -*- coding: utf-8 -*-
"""
February 2018
Binary trees: occurrences and hierarchical numbering
@author: Nathalie
"""

from algopy import bintree
from algopy import queue

#------------------------------------------------------------------------------
# 5.1                           Occurrence list display

# with BFS (parcours largeur)

def treeToOccList(B):
    '''
    Builds the list of node occurrences
    '''
    q = queue.Queue()
    q.enqueue((B,""))
    L = []
    while not q.isempty():
        (T, occ) = q.dequeue()
        L.append(occ)
        if T.left != None:
            q.enqueue((T.left, occ+'0'))
        if T.right != None:
            q.enqueue((T.right, occ+'1'))
    return L      

def printOccList(B):
    '''
    Prints the occurrence list representation of B
    '''
    if B != None:
        L = treeToOccList(B)
        s = '{' + chr(949)  # 'ε'
        for i in range(1, len(L)):
            s += ", " + L[i]
        s += '}'
    print(s)            
         
    

#------------------------------------------------------------------------------
# 5.2                         Prefix code

# tree from 5.2 q 3
        
codeTree = BinTree(None,
                   BinTree('a',None,None),
                   BinTree(None,
                          BinTree(None,BinTree('c',None,None),BinTree('b',None,None)),
                          BinTree(None,
                                 BinTree(None,BinTree('f',None,None),BinTree('e',None,None)),
                                 BinTree('d',None,None))))

occ = "{ε, 0, 1, 10, 11, 100, 101, 110, 111, 1100, 1101}"


# not in tutorial

def listCodes(B):
    '''
    Builds the list of (letter, code)
    B is not None 
    B is full (localement complet)
    '''
    q = queue.Queue()
    q.enqueue((B,""))
    L = []
    while not q.isempty():
        (T, occ) = q.dequeue()
        if T.left == T.right:
            L.append((T.key, occ))
        else:
            q.enqueue((T.left, occ+'0'))
            q.enqueue((T.right, occ+'1'))
    return L      


# same with DFS (parcours profondeur)


def __listCodesDFS(T, L, code=""):
    if T.left == T.right:
        L.append((T.key, code))
    else:
        __listCodesDFS(T.left, L, code + '0')
        __listCodesDFS(T.right, L, code + '1')

def listCodesDFS(T):
    '''
    Builds the list of (letter, code)
    B is not None 
    B is full (localement complet)
    '''
    L = []
    __listCodesDFS(T, L)
    return L


#  q 4
    
def findCode(T, letter, code=''):
    '''
    Find the code of letter
    B is not None 
    B is full (localement complet)
    '''
    if T.left == T.right:
        if T.key == letter:
            return code
        else:
            return None
    else:
        res = findCode(T.left, letter, code + '0')
        if res != None:
            return res
        else:
            return findCode(T.right, letter, code + '1')
        
# same but the code is built going up!
def findCode2(T, letter):
    if T.left == T.right:
        if T.key == letter:
            return ""
        else:
            return None
    else:
        res = findCode2(T.left, letter)
        if res != None:
            return '0' + res
        else:
            res = findCode2(T.right, letter)
            if res != None:
                return '1' + res
            else:
                return None
            


"""
Hierarchical numbering
"""
#------------------------------------------------------------------------------
             
''' 
Trees as vector (list here) : 
using the hierarchical numbering
T[i] is the value at node number i (T[0] unused...)
'''


#------------------------------------------------------------------------------
#                             Examples


B = BinTree(22, 
            BinTree(5, 
                    BinTree(3, BinTree(1, None, None), BinTree(4, None, None)), 
                    BinTree(12, None, BinTree(17, None, None))), 
            BinTree(29, BinTree(23, None, None), None))

# the "hierarchical" representation of tree B:
L = [None, 22, 5, 29, 3, 12, 23, None, 1, 4, None, 17, None, None, None, None, None, None, None, None, None, None, None, None]

# another example:

T_hier = [None]*30
for i in range(1, 9):
    T_hier[i] = i
(T_hier[11], T_hier[14], T_hier[29]) = (11, 14, 29)

#------------------------------------------------------------------------------
#  5.3                 Classics written with hierarchical representation

def size_h(T, i = 1):
    if (i >= len(T)) or (T[i] == None):
        return 0
    else:
        return 1 + size_h(T, 2*i) + size_h(T, 2*i+1)
        
def depth_pref_h(T, i = 1):
    if (i < len(T)) and (T[i] != None):
        print(T[i], end=' ')
        depth_pref_h(T, 2*i)
        depth_pref_h(T, 2*i+1)

def breadth(T):
    if len(T) > 1 and T[1] != None:
        l = len(T)
        q = queue.Queue()
        q.enqueue(1)
        while not q.isempty():
            no = q.dequeue()
            print(T[no])
            if no < l and T[no] != None:   # left child
                q.enqueue(2 * no)
            if no < l and T[no] != None:   # right child
                q.enqueue(2 * no + 1)

    
#------------------------------------------------------------------------------           
#  5.4                     object implementation <-> hierarchical (list)
     
# from BinTree to hierarchical representation

# version1: the size is given (maxi)

def __hierFromTree(B, T, maxi, i = 1):
    if i >= maxi:
        raise Exception("array is too short")
    if B == None:
        T[i] = None
    else:
        T[i] = B.key
        __hierFromTree(B.left, T, maxi, 2*i)
        __hierFromTree(B.right, T, maxi, 2*i+1)

def hierFromTree(B, maxi):
    T = [None]*maxi  
    __hierFromTree(B, T, maxi)
    return T

# version2: the list grows when needed (thanks to GolluM)

def extendList(L, i):
    for _ in range(len(L), i+1):
        L.append(None)
        
def __tree2hier(B, L, i = 1):
    if B !=  None:
        extendList(L, i)
        L[i] = B.key
        __tree2hier(B.left, L, 2 * i)
        __tree2hier(B.right, L, 2 * i + 1)
    
def tree2hier(B):
    L = [None]
    __tree2hier(B, L)
    return L
    
# q2: list -> object
# from hierarchical representation to BinTree

def hier2tree(L, i = 1):
    if i >= len(L) or L[i] == None:
        return None
    else:
        B = bintree.BinTree(L[i], None, None)
        B.left = hier2tree(L, 2*i)
        B.right = hier2tree(L, 2*i+1)
        return B
    
#       return BinTree(T[i], treeFromHier2(T, 2*i), treeFromHier2(T, 2*i+1))
    
    

