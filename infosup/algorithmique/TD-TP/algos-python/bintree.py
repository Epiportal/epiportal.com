# -*- coding: utf-8 -*-
"""Binary Tree module"""


class BinTree:
    """Simple class for binary tree

    Attributes:
        key (Any): Node key.
        left (BinTree): Left child.
        right (BinTree): Right child.

    """

    def __init__(self, key, left, right):
        """Init binary tree.

        Args:
            key (Any): Node key.
            left (BinTree): Left child.
            right (BinTree): Right child.

        """

        self.key = key
        self.left = left
        self.right = right


