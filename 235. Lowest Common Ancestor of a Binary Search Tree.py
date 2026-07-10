"""
LeetCode #235 - Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in
the BST.

According to the definition of LCA on Wikipedia: "The lowest
common ancestor is defined between two nodes p and q as the lowest node in T that has
both p and q as descendants (where we allow a node to be a descendant of itself)."

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

*

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes `2` and `8` is `6`.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes `2` and `4` is `2`, since a node can be a descendant of itself according to the LCA definition.

Note:

All of the nodes' values will be unique.

p and q are different and both values will exist in the BST.
"""

from typing import List, Optional


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用 BST 的性质：左子树所有节点值 < 根节点值 < 右子树所有节点值。
# 从根节点开始迭代查找：
# - 如果 p 和 q 的值都小于当前节点值，说明 LCA 一定在左子树中，向左走。
# - 如果 p 和 q 的值都大于当前节点值，说明 LCA 一定在右子树中，向右走。
# - 否则(一个小于等于，一个大于等于，或其中之一等于当前节点)，
#   当前节点就是 p 和 q 的分叉点，即为 LCA，直接返回当前节点。
# 由于题目保证 p 和 q 一定存在于树中，不需要额外的空值检查。
#
# 时间复杂度: O(H) - 其中 H 是树的高度，最坏情况退化成链表 O(n)
# 空间复杂度: O(1) - 迭代方式不使用额外空间(递归则为 O(H))
#
# 关键点:
# - 利用 BST 值的大小性质，无需遍历整棵树
# - 当 p 和 q 分别在当前节点两侧时，当前节点就是 LCA
# - 迭代实现空间 O(1)，优于递归的 O(H)
# - 与 #236(普通二叉树 LCA) 的区别：本解法利用 BST 有序性简化判断
