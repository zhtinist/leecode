"""
LeetCode #95 - Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/

Given an integer n, return all the structurally unique BST's (binary search
trees), which has exactly n nodes of unique values from 1 to n.

Example 1:
    Input: n = 3
    Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
    Input: n = 1
    Output: [[1]]

Constraints:
    1 <= n <= 8
"""

from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            trees = []
            for root_val in range(start, end + 1):
                for left in build(start, root_val - 1):
                    for right in build(root_val + 1, end):
                        trees.append(TreeNode(root_val, left, right))
            return trees

        return build(1, n)
