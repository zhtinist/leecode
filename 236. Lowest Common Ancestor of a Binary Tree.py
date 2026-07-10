"""
LeetCode #236 - Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the
tree.

According to the definition of LCA on Wikipedia: "The lowest
common ancestor is defined between two nodes p and q as the lowest node in T that
has both p and q as descendants (where we allow a node to be a descendant of
itself)."

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

*

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes `5` and `1` is `3.`

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes `5` and `4` is `5`, since a node can be a descendant of itself according to the LCA definition.

Note:

All of the nodes' values will be unique.

p and q are different and both values will exist in the binary tree.
"""

from typing import List, Optional


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归分治法(后序遍历)。
# 从根节点开始递归：
# 1. 终止条件: 若 root 为空，或 root == p，或 root == q，直接返回 root。
#    这意味着在子树中找到了 p 或 q，将结果向上传递。
# 2. 分别在左子树和右子树中递归查找 p 和 q。
# 3. 根据左右子树的返回结果判断：
#    - 若左右子树都返回非空：说明 p 和 q 分别在当前节点的两侧子树中，
#      当前节点就是 LCA，返回 root。
#    - 若只有一侧返回非空：说明 p 和 q 都在那一侧，返回非空的那一侧结果。
#    - 若两侧都为空：说明当前子树不包含 p 或 q，返回 None。
# 此解法的核心思想是自底向上传递找到的 p/q 节点，
# 当某个节点的左右子树各包含 p 和 q 时，该节点就是 LCA。
#
# 时间复杂度: O(n) - 最坏情况下需要访问所有节点
# 空间复杂度: O(H) - 递归栈深度，最坏情况退化成链表 O(n)
#
# 关键点:
# - 利用递归后序遍历，自底向上汇总信息
# - root == p or root == q 的终止条件允许节点自身是 LCA
# - 当 left 和 right 都非空时，当前 root 就是 LCA，此后所有上层调用都接收这个结果
# - 与 #235(BST LCA) 的区别：本解法通用但复杂，不依赖节点值的比较
