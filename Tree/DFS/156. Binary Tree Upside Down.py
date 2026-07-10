"""
LeetCode #156 - Binary Tree Upside Down
https://leetcode.com/problems/binary-tree-upside-down/

Given the root of a binary tree, turn the tree upside down and return the new
root.

You can turn a binary tree upside down with the following rules:
1. The original right child should become the new left child.
2. The original left child should become the new root.
3. The original parent should become the new right child.

Example 1:
    Input: root = [1,2,3,4,5]
    Output: [4,5,2,null,null,3,1]

Example 2:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 10].
    -100 <= Node.val <= 100
    The values of the nodes in the tree are unique.
    root is a binary search tree.
"""

from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None

        return new_root
