"""
LeetCode #1372 - Longest ZigZag Path in a Binary Tree
中文题名：二叉树中最长的交错路径
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

Given a binary tree `root`, a ZigZag path for a binary tree is
defined as follow:

Choose any node in the binary tree and a direction (right or
left).

If the current direction is right then move to the right child of the current
node otherwise move to the left child.

Change the direction from right to left or right to left.

Repeat the second and third step until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a
length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0

Constraints:

Each tree has at most `50000` nodes..

Each node's value is between `[1, 100]`.

【中文翻译】
给定一棵二叉树 `root`，二叉树的 ZigZag 路径定义如下：

选择二叉树中的任意节点和一个方向（向右或向左）。
如果当前方向是向右，则移动到当前节点的右子节点；否则移动到左子节点。
改变方向（从右到左或从左到右）。
重复第二步和第三步，直到无法在树中移动。

ZigZag 长度定义为访问的节点数减 1（单个节点的长度为 0）。

返回该树中最长 ZigZag 路径的长度。

示例 1：
输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：最长 ZigZag 路径如蓝色节点所示（右 -> 左 -> 右）。

示例 2：
输入：root = [1,1,1,null,1,null,null,1,1,null,1]
输出：4
解释：最长 ZigZag 路径如蓝色节点所示（左 -> 右 -> 左 -> 右）。

示例 3：
输入：root = [1]
输出：0
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node: Optional[TreeNode], direction: int, length: int):
            """
            direction: 0 -> 当前来自左子节点（下一步应该向右）
            direction: 1 -> 当前来自右子节点（下一步应该向左）
            """
            if not node:
                return
            self.max_len = max(self.max_len, length)

            if direction == 0:
                # 上一步走了左边，这一步应走右边延续 zigzag
                dfs(node.right, 1, length + 1)
                # 也可以从这里重新开始走左边
                dfs(node.left, 0, 1)
            elif direction == 1:
                # 上一步走了右边，这一步应走左边延续 zigzag
                dfs(node.left, 0, length + 1)
                # 也可以从这里重新开始走右边
                dfs(node.right, 1, 1)

        if root:
            dfs(root.left, 0, 1)   # 从根向左走
            dfs(root.right, 1, 1)  # 从根向右走

        return self.max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 深度优先搜索（DFS），在每个节点记录当前方向和当前路径长度。
# direction: 0 表示上一步从父节点向左到达当前节点（下一步应向右），
#           1 表示上一步从父节点向右到达当前节点（下一步应向左）。
# 对于每个节点，有两种选择：
# 1. 延续 zigzag：按交替方向继续向下（长度+1）。
# 2. 重新开始：以当前节点为起点，向另一个方向走（长度重置为1）。
# 全局变量 max_len 记录遍历过程中遇到的最大长度。
#
# 时间复杂度: O(N)，N 为节点数，每个节点被访问常数次
# 空间复杂度: O(H)，H 为树高（递归栈深度）
#
# 关键点:
# - direction 参数追踪当前方向以便决定下一步走左还是右
# - 每个节点可以"延续"zigzag 或"重新开始"zigzag
# - 从根节点开始分别向左和向右启动 DFS













