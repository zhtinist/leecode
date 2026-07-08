"""
LeetCode #99 - Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

You are given the root of a binary search tree (BST), where the values of exactly
two nodes of the tree were swapped by mistake. Recover the tree without changing
its structure.

Example 1:
    Input: root = [1,3,null,null,2]
    Output: [3,1,null,null,2]

Example 2:
    Input: root = [3,1,4,null,null,2]
    Output: [2,1,4,null,null,3]

Constraints:
    The number of nodes in the tree is in the range [2, 1000].
    -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        current = root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev and current.val < prev.val:
                second = current
                if not first:
                    first = prev
                else:
                    break
            prev = current
            current = current.right

        first.val, second.val = second.val, first.val
