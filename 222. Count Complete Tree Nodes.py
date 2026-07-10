"""
LeetCode #222 - Count Complete Tree Nodes
中文题名：完全二叉树的节点个数
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:

In a complete binary tree every level, except possibly the last, is completely filled, and
all nodes in the last level are as far left as possible. It can have between 1 and
2^h nodes inclusive at the last level h.

Example:

Input:
1
/ \
2   3
/ \  /
4  5 6

Output: 6

【中文翻译】
给你一棵完全二叉树的根节点 root，求出该树的节点个数。

注意：

完全二叉树的定义来自维基百科：

在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1 到 2^h 个节点。

示例：

输入：
1
/ \
2   3
/ \  /
4  5 6

输出：6
"""

from typing import List, Optional


class Solution:
    def countNodes(self, root: Optional['TreeNode']) -> int:
        if not root:
            return 0

        left_depth = 0
        node = root
        while node:
            left_depth += 1
            node = node.left

        right_depth = 0
        node = root
        while node:
            right_depth += 1
            node = node.right

        if left_depth == right_depth:
            return (1 << left_depth) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)












# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 利用完全二叉树的性质进行二分查找。
# 1. 分别计算左子树最左路径的深度(left_depth)和右子树最右路径的深度(right_depth)。
# 2. 若 left_depth == right_depth，说明该树是满二叉树(完美二叉树)，
#    节点总数 = 2^depth - 1，可直接公式计算。
# 3. 若不等，说明最后一层不满，递归计算左子树和右子树的节点数：
#    总节点数 = 1(根) + countNodes(root.left) + countNodes(root.right)。
# 4. 由于完全二叉树的特性，每次递归必有一边是满二叉树可用公式计算，
#    递归深度为 O(log n)，每次计算深度为 O(log n)。
#
# 时间复杂度: O(log^2 n) - 每次递归计算深度 O(log n)，最多递归 O(log n) 层
# 空间复杂度: O(log n) - 递归栈深度
#
# 关键点:
# - 完全二叉树：除了最后一层，其余层都是满的，最后一层从左到右填充
# - 满二叉树节点数 = 2^h - 1，可 O(1) 计算
# - 每次递归至少有一半是满二叉树，大大减少计算量
# - 位运算 (1 << depth) 比 pow(2, depth) 更高效
