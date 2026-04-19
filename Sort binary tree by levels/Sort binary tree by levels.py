"""
Module for Sort binary tree by levels
"""

class Node:
    """
    Module for Node
    """

    def __init__(self, L, R, n):
        """
        Module for __init__
        """

        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    """
    Module for tree_by_levels
    """

    if not node:
        return []

    fringe = []
    lst = []
    fringe.append(node)

    while fringe:
        p = fringe.pop(0)
        lst.append(p.value)

        if isinstance(p.left, Node):
            fringe.append(p.left)

        if isinstance(p.right, Node):
            fringe.append(p.right)

    return lst

