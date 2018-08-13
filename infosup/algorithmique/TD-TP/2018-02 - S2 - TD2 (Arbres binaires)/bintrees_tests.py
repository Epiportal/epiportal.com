from algo import bintree, queue


# equality test

def equal(B1, B2):

    if B1 == None:
        return B2 == None
    elif B2 == None:
        return False
    elif B1.key == B2.key:
        return equal(B1.left, B2.left) and equal(B1.right, B2.right)
    else:
        return False
        
def equal2(B1, B2):
    if B1 == None or B2 == None:
        return B1 == B2
    else:
        return (B1.key == B2.key) \
               and equal2(B1.left, B2.left) \
               and equal2(B1.right, B2.right)

#------------------------------------------------------------------------------

# isSubTree(sB, B): tests if sB is a subtree of B

def search(x, B):
    if B == None:
        return None
    elif x == B.key:
        return B
    else:
        R = search(x, B.left)
        if R == None:
            R = search(x, B.right)
        return R
        
def isSubTree(sB, B):
    if sB == None:           
        return True
    else:
        R = search(sB.key, B)
        return equal(sB, R)
    
def isSubTree2(sB, B):
    if sB == None:
        return True
    elif B == None:
        return False
    else:
        if sB.key == B.key:
            return equal(sB, B)
        else:
            return isSubTree2(sB, B.left) or isSubTree2(sB, B.right)
            
#-------------------------------------------------------------
            


def __symmetric(B1, B2):
    if B1 == None or B2 == None:
        return B1 == B2
    else:
        if B1.key != B2.key:
            return False
        else:
            return __symmetric(B1.left, B2.right) \
                   and __symmetric(B1.right, B2.left)

def symmetric(B):
    return B == None or __symmetric(B.left, B.right)
    
    

#-------------------------------------------------------------

def degenerate0(T):
    if T == None :
        return True
    elif T.left != None  and T.right != None :
        return False 
    else :
        return degenerate0(T.left) and degenerate0(T.right)
        
        
def __degenerate(B):
    '''
    B not empty
    '''
    if B.left == None:
        if B.right == None:
            return True
        else:
            return __degenerate(B.right)
    else:
        if B.right == None:
            return __degenerate(B.left)
        else:
            return False
            
def degenerate(B):
    return B == None or __degenerate(B)


def __degenerate2(B):
    '''
    B not empty
    '''
    leftEmpty = (B.left == None)
    if B.right == None:
        return leftEmpty or __degenerate2(B.left)
    else:
        return leftEmpty and __degenerate2(B.right)
        
def degenerate2(B):
    return B == None or __degenerate2(B)

    
    
#------------------------------------------------------------------------------        

def __leftlength(B):
    """
    returns the length of the left branch
    """
    h = -1
    T = B
    while T != None:
        h += 1
        T = T.left
    return h
    
def __perfect(B, h):
    '''
    B != None
    '''
    if B.left == None:
        if B.right == None:
            return h == 0
        else:
            return False
    else:
        if B.right == None:
            return False
        else:
            return __perfect(B.left, h-1) and __perfect(B.right, h-1)
        
def perfect(B):
    if B == None:
        return True
    else:
        return __perfect(B, __leftlength(B))



def __perfect2(B, h):
    if B== None:
        return h == -1
    else:
        return __perfect2(B.left, h-1) and __perfect2(B.right, h-1)
    
def perfect2(B):
    return __perfect2(B, __leftlength(B))    


def __perfect3(B, h):
    if B.left != None and B.right != None:
        return __perfect3(B.left, h-1) and __perfect3(B.right, h-1)
    else:
        return (B.left == None and B.right == None) and (h == 0)
    
def perfect3(B):
    return B == None or __perfect3(B, __leftlength(B))
    

# version that compute the height going up

def __perfectup(B):
    if B.left == B.right:
        return (True, 0)
    else:
        if B.left == None or B.right == None:
            return (False, -42)
        else:
            (okLeft, hLeft) = __perfectup(B.left)
            if not okLeft:
                return (False, -42)
            else:
                (okRigh, hRight) = __perfectup(B.right)
                return (okRigh and hLeft == hRight, hLeft + 1)

def isperfect_up(B):
    if B == None:
        return True
    else:
        (ok, _) = __perfectup(B)
        return ok


def perfectWidth(B):
    """
    BFS: tests if each level has twice as many nodes 
    as the previous level
    """
    if B == None:
        return True
    else:
        q = queue.Queue()
        q = queue.enqueue(B, q)
        q = queue.enqueue(None, q)
        (w, next_w) = (0, 1)
        perfect = True
        while not queue.isEmpty(q) and perfect:
            T = queue.dequeue(q)
            if T == None:
                if w != next_w:
                    perfect = False
                if not queue.isEmpty(q):
                    next_w = w * 2
                    w = 0
                    q = queue.enqueue(None, q)
            else:
                w = w + 1
                if T.left != None:
                    q = queue.enqueue(T.left, q)
                if T.right != None:
                    q = queue.enqueue(T.right, q)
        return perfect

#------------------------------------------------------------------

def completeWidth(B):
    q = queue.Queue()
    q = queue.enqueue(B, q)
    empty_child = False
    while not queue.isEmpty(q) and not empty_child:
        T = queue.dequeue(q)
        if T.left == None:
            empty_child = True
        else:
            q = queue.enqueue(T.left, q)
            if T.right != None:
                q = queue.enqueue(T.right, q)
            else:
                empty_child = True
    complete = True
    while not queue.isEmpty(q) and complete:
        T = queue.dequeue(q)
        complete = (T.left == None and T.right == None)
    return complete
    
