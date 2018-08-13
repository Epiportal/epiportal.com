# -*- coding: utf-8 -*-
"""
examples of binary trees
"""

from algopy import bintree
from algopy.bintree import BinTree # to avoid writing bintree.BinTree!

B_ex = BinTree(1, 
          BinTree(2, 
                BinTree(4, BinTree(8,None,None), None), 
                BinTree(5,None,BinTree(11,None,None))),
          BinTree(3, 
                BinTree(6,None,None), 
                BinTree(7, BinTree(14,None,BinTree(29,None,None)),None)))
         
B_tuto = BinTree('V', 
            BinTree('D', 
               BinTree('I', 
                  BinTree('Q', None,BinTree('U', None,None)),
                  None),
               BinTree('S', 
                  BinTree('E', None,None),
                  BinTree('T', None,None))),
            BinTree('I', 
               BinTree('E', 
                  None,
                  BinTree('R', None,None)),
              BinTree('A', 
                  BinTree('T', None,None),
                  BinTree('S', None,None))))         
