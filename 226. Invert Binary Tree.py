"""
LeetCode #226 - Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

4
/   \
2     7
/ \   / \
1   3 6   9

Output:

4
/   \
7     2
/ \   / \
9   6 3   1

Trivia:

This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can't
invert a binary tree on a whiteboard so f*** off.
"""

from typing import List, Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 递归翻转二叉树。对于每个节点:
# - 递归翻转左子树和右子树
# - 交换当前节点的左右孩子
# 基准条件: 根节点为 None 时直接返回 None
# 通过 Python 的多重赋值一行完成交换:
# root.left, root.right = invertTree(root.right), invertTree(root.left)
# 这样做既翻转了子树，又交换了位置。
#
# 时间复杂度: O(n) - 每个节点访问一次
# 空间复杂度: O(h) - 递归栈深度为树高，最坏 O(n) (退化成链表)，最好 O(log n) (平衡树)
#
# 关键点:
# - 递归的基准条件必不可少，否则遇到叶子节点会出错
# - 多重赋值确保交换是原子操作，不会因顺序问题出错
# - 也可以用 BFS/DFS 迭代实现，但递归最简洁
