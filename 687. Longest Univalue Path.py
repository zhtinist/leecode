"""
LeetCode #687 - Longest Univalue Path
中文题名：最长同值路径
https://leetcode.com/problems/longest-univalue-path/

Given a binary tree, find the length of the longest path where each node in the path has the
same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

5
/ \
4   5
/ \   \
1   1   5

Output: 2

Example 2:

Input:

1
/ \
4   5
/ \   \
4   4   5

Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is
not more than 1000.

【中文翻译】
给定一棵二叉树，找到最长路径的长度，该路径中的每个节点具有相同的值。这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度由它们之间的边数表示。

示例 1：

输入：

      5
     / \
    4   5
   / \   \
  1   1   5

输出: 2

示例 2：

输入：

      1
     / \
    4   5
   / \   \
  4   4   5

输出: 2

注意：给定的二叉树不超过 10000 个节点。树的高度不超过 1000。
"""

from typing import List, Optional


class Solution:
    def longestUnivaluePath(self, root: Optional['TreeNode']) -> int:
        self.ans = 0

        def dfs(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        dfs(root)
        return self.ans









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 递归，自底向上计算。
# 定义 dfs(node) 返回从 node 出发向下的最长同值路径长度（边数）。
# 对于当前节点：
# - 递归计算左右子树的返回长度。
# - 如果左子节点存在且值等于当前节点值，则左箭长度 = 左子树返回值 + 1（连接当前边）。
# - 右箭头类似处理。
# - 更新全局答案：max(ans, 左箭长度 + 右箭长度)，即经过当前节点的路径。
# - 返回 max(左箭长度, 右箭长度) 给父节点使用（路径不能分叉）。
#
# 时间复杂度: O(N) - 每个节点访问一次
# 空间复杂度: O(H) - 递归栈深度，H 为树的高度
#
# 关键点:
# - 返回单边最长路径（不能分叉），但答案可以合并左右
# - 只有当子节点值与当前节点值相等时才延长路径
# - 全局变量 ans 追踪经过每个节点的最长路径
