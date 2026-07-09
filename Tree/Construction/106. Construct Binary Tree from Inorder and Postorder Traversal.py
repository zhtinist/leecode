"""
LeetCode #106 - Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the
same tree, construct and return the binary tree.

Example 1:
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]

Example 2:
    Input: inorder = [-1], postorder = [-1]
    Output: [-1]

Constraints:
    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree.
"""

from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_index = {val: i for i, val in enumerate(inorder)}

        def build(in_start: int, in_end: int, post_start: int, post_end: int) -> Optional[TreeNode]:
            if in_start > in_end:
                return None

            root_val = postorder[post_end]
            root = TreeNode(root_val)
            mid = in_index[root_val]
            left_size = mid - in_start

            root.left = build(in_start, mid - 1, post_start, post_start + left_size - 1)
            root.right = build(mid + 1, in_end, post_start + left_size, post_end - 1)
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
