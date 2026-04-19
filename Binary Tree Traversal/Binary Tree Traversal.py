"""
Module for Binary Tree Traversal
"""

class Node:
    """
    Module for Node
    """

    def __init__(self, name):
        """
        Module for __init__
        """

        self.data = name
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):
    """
    Module for pre_order
    """

    if not node:
        return []

    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    """
    Module for in_order
    """

    if not node:
        return []

    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    """
    Module for post_order
    """

    if not node:
        return []

    return post_order(node.left) + post_order(node.right) + [node.data]

