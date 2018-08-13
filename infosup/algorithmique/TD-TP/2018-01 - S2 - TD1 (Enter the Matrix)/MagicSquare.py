# -*- coding: utf-8 -*-
"""
Magic Squares
January 2016
@author: Nathalie
"""



S5 = [[17, 24, 1, 8, 15],
      [23, 5, 7, 14, 16], 
      [4, 6, 13, 20, 22], 
      [10, 12, 19, 21, 3], 
      [11, 18, 25, 2, 9]]
    

def SumLine(L):
    b = len(L)
    c = 0
    for i in range(b):
        c+= L[i]
    return c

def SumColonne(A,b):
    c = len(A)
    d = 0
    for i in range(c):
        d += A[i][b]
    return d

def Sumdiag(A):
    a = len(A)
    c = 0
    for i in range(a):
        c += A[i][i]
    return c

def Sumdiag2(A):
    a = len(A[0])
    n = a
    b = 0
    c = 0
    for i in range(n):
        c += A[a-1][b]
        a -= 1
        b += 1
    return c


def magic_square(A):
    n = len(A)
    if n!= len(A[0]):
        raise Exception("fghjk")
    c = Sumdiag(A)
    d = Sumdiag2(A)
    t = False
    i = 0
    while i < n and c == d:
        d = SumLine(A[i])
        i += 1
    i = 0
    while i < n and c == d:
        d = SumColonne(A,i)
        i += 1
    if c ==d:
        t = True
    return t 
        


# a single function:

def testMagic(S):
    n = len(S)
    if S == [] or n != len(S[0]):
        raise Exception("Empty or not a square")
    (diag1, diag2) = (0, 0)
    for i in range(n):
        diag1 = diag1 + S[i][i]
        diag2 = diag2 + S[i][n-i-1]
    if diag1 != diag2:
        return False
    else:
        magic = diag1
        sum_l = magic
        sum_c = magic
        i = 0
        while (i < n) and (sum_l == magic and sum_c == magic):
            sum_l = 0
            sum_c = 0
            for j in range(n):
                sum_l = sum_l + S[i][j]
                sum_c = sum_c + S[j][i]
            i = i + 1
        return i == n 



def testNormal(S):
    n = len(S)    
    n2 = n * n
    L = []
    for i in range(n2):
        L.append(False)
    ok = True
    i = 0
    while (i < n) and ok:
        j = 0
        while (j < n) and ok:
            if (S[i][j] <= 0) or (S[i][j] > n2) \
                or L[S[i][j]-1]:
                ok = False
            else:
                L[S[i][j]-1] = True
            j = j + 1
        i = i + 1
    return ok


from algopy import matrix

def Siamise(n):
    """
    builds a magic square of n-odd size
    starts in the middle of last line, then going SE
    """
    S = matrix.init(n, n, 0)
    i = n-1
    j = n // 2
    S[i][j] = 1
    for k in range(2, n*n + 1):
        i2 = (i + 1) % n
        j2 = (j + 1) % n
        if S[i2][j2] == 0:
            (i, j) = (i2, j2)
        else:
            i = i-1
            if i == -1:
                i = n-1
        S[i][j] = k
    return S

