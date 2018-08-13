from algopy import bintree

class BinTreeSize:
    def __init__(self, key, left, right, size):
        self.key = key
        self.left = left
        self.right = right
        self.size = size


#------------------------------------------------------------------------------
# copyWithSize

def __addSize(B):
    if B == None:
        return(None, 0)
    else:
        C = BinTreeSize(B.key, None, None, 1)
        (C.left, size1) = __addSize(B.left)
        (C.right, size2) = __addSize(B.right)
        C.size += size1 + size2
        return (C, C.size)        

def __addSize2(B):
    if B == None:
        return(None, 0)
    else:
        (left, size1) = __addSize2(B.left)
        (right, size2) = __addSize2(B.right)
        size = 1 + size1 + size2
        return (BinTreeSize(B.key, left, right, size), size)
                
def copyWithSize(B):
    (C, size) = __addSize(B)
    return C
    
