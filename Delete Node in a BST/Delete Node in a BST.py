"""
Module for Delete Node in a BST
"""

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    """
    Module for TreeNode
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Module for __init__
        """

        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Module for Solution
    """

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Module for deleteNode
        """

        if not root:
            return root

        probe = root
        prev = probe

        while probe:

            if probe.val == key:
                break

            prev = probe

            if probe.val > key:
                probe = probe.left if isinstance(probe.left, TreeNode) else None

            else:
                probe = probe.right if isinstance(probe.right, TreeNode) else None

        if not probe:
            return root

        if not isinstance(probe.left, TreeNode) and not isinstance(probe.right, TreeNode):

            if probe == root and probe.val == 0:
                return None

            if prev.left == probe:
                prev.left = None

            else:
                prev.right = None

        elif isinstance(probe.right, TreeNode) and not isinstance(probe.left, TreeNode):

            if probe == root:
                root = probe.right

            if prev.left == probe:
                prev.left = probe.right

            else:
                prev.right = probe.right

        elif isinstance(probe.left, TreeNode) and not isinstance(probe.right, TreeNode):

            if probe == root:
                root = probe.left

            if prev.left == probe:
                prev.left = probe.left

            else:
                prev.right = probe.left

        else:
            prev1 = probe
            probe1 = probe.left
            check = False

            while probe1.right:
                check = True
                prev1 = probe1
                probe1 = probe1.right

            if check:
                prev1.right = probe1.right if probe1.right else probe1.left

            else:
                prev1.left = probe1.right if probe1.right else probe1.left

            probe.val = probe1.val

        return root
