# -*- coding: utf-8 -*-
"""
Nov. 2017
@author: Nathalie
"""

#----------------------- ex 1.1 -----------------------------------------------
def zorglub(n):
    '''
    Returns the sum of i! (i:1..n)
    '''
    f = 1
    s = 0
    i = 1
    while i <= n:
        f = f * i
        s = s + f
        i = i + 1
    return s

#----------------------- ex 1.2 -----------------------------------------------

def product(a, b):
    '''
    calcultates a * b (without *)
    '''
    if a == 0:
        return 0
    elif a == 1:
        return b
    elif a == -1:
        return -b
    else:
        if b < 0:
            b = -b   # (a, b) = (-a, -b)
            a = -a
        p = 0
        i = 1
        while i <= b:
            p = p + a
            i = i + 1
        return p
    # can also be done with b = b - 1 till b = 0: see power

#----------------------- ex 1.3 -----------------------------------------------

def power(x, n):
    '''
    calculates x**n, n natural
    # here 0**0 = 1...
    '''
    if n < 0:
        raise Exception("n not a natural")
    if x == 0:
        if n == 0:
            return 1
        else:
            return 0
    elif x == 1:
        return 1
    elif x == -1:
        return 1 + (n % 2) * (-2)
    else:
        p = 1
        while n > 0:
            p = p * x
            n = n - 1
        return p



#----------------------- ex 1.4 -----------------------------------------------
    
def fibo(n):
    fi_2 = 1    # or 0 if f(0) = 0
    fi_1 = 1
    i = 2
    while i <= n:
        fi = fi_1 + fi_2
        i = i + 1
        fi_2 = fi_1
        fi_1 = fi
    return fi

def fibo2(n):
    (fi_1, fi) = (1, 1)    # or (0, 1) if f(0) = 0
    while n > 1:
        (fi_1, fi) = (fi, fi + fi_1)
        n = n - 1
    return fi

def fibo3(n):
    a = 1
    b = 1
    while n > 1:
       a = a + b
       b = a + b
       n = n - 2
       print(a, b)
    if n % 2 == 0:
        return a
    else:
        return b

#----------------------- ex 1.5 -----------------------------------------------
       
def u(i):
    return 3*i + 2

def sum(n):
    s = 0
    i = 1
    while i <= n:
        s = s + u(i)
        i = i + 1
    return i

def sumSums(n):
    sumS = 0
    i = 1
    while i <= n:
        s = 0
        j = 1
        while j <= i:
            s = s + u(j)
            j = j + 1
        sumS = sumS + s
        i = i + 1
    return sumS

def sumSums2(n):
    s = 0
    sumS = 0
    i = 1
    while i <= n:
        s = s + u(i)      # or sumS = sumS + (n-i+1) * u(i)
        sumS = sumS + s
        i = i + 1
    return sumS
    
"""
for loop
"""

# power without special cases

def power2(x, n):
    p = 1
    for i in range(n):
        p = p * x
    return p
    

# sums
def sumSums2_(n):
    s = 0
    sumS = 0
    for i in range(1, n+1):
        s = s + u(i)      # or sumS = sumS + (n-i+1) * u(i)
        sumS = sumS + s
    return sumS
