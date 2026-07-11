"""
LeetCode #298 - Binary Tree Longest Consecutive Sequence
中文题名：二叉树最长连续序列
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree
along the parent-child connections. The longest consecutive path need to be from parent to
child (cannot be the reverse).

Example 1:

Input:

1
\
3
/ \
2   4
\
5

Output: `3`

Explanation: Longest consecutive sequence path is `3-4-5`, so return `3`.

Example 2:

Input:

2
\
3
/
2
/
1

Output: 2

Explanation: Longest consecutive sequence path is `2-3`, not `3-2-1`, so return `2`.

【中文翻译】
给定一个二叉树，找出最长连续序列路径的长度。

路径指的是从某个起始节点到树中任意节点的序列，沿着父-子连接。最长连续路径需要从父节点到子节点（不能反向）。

示例 1：

输入：

1
\
3
/ \
2   4
\
5

输出：`3`

解释：最长连续序列路径是 `3-4-5`，所以返回 `3`。

示例 2：

输入：

2
\
3
/
2
/
1

输出：2

解释：最长连续序列路径是 `2-3`，而不是 `3-2-1`，所以返回 `2`。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """Find the length of the longest consecutive sequence path (parent->child).

        DFS approach: pass down the expected next value and current length.
        Track the global maximum.
        """
        self.max_len = 0

        def dfs(node: TreeNode, parent_val: int, cur_len: int):
            if not node:
                return

            # Check if this node continues the consecutive sequence
            if node.val == parent_val + 1:
                cur_len += 1
            else:
                cur_len = 1

            self.max_len = max(self.max_len, cur_len)

            # Recurse with current node as parent
            dfs(node.left, node.val, cur_len)
            dfs(node.right, node.val, cur_len)

        if not root:
            return 0
        dfs(root, root.val - 1, 0)  # start: root will always be length 1
        return self.max_len


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# DFS 递归。自上而下传递两个参数：
# - parent_val：父节点的值
# - cur_len：以当前节点结尾的连续递增序列长度
#
# 如果 node.val == parent_val + 1，则当前节点延续了序列，cur_len += 1；
# 否则从当前节点重新开始，cur_len = 1。
# 用全局变量 max_len 记录所有节点处的最长路径长度。
# 注意：路径只能从父到子方向，不能反过来。
#
# 时间复杂度: O(N) - 每个节点访问一次
# 空间复杂度: O(H) - 递归栈深度，最坏 O(N)，平衡树 O(log N)
#
# 关键点:
# - 路径方向必须是父 -> 子（自顶向下），不能反向
# - 不要求从根开始到叶结束，任意路径都可以
# - cur_len 记录的是以当前节点结尾的连续长度
# - 条件: node.val == parent_val + 1
# - 使用实例变量 self.max_len 跟踪全局最大值
