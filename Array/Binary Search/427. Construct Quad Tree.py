"""
LeetCode #427 - Construct Quad Tree
中文题名：建立四叉树
https://leetcode.com/problems/construct-quad-tree/

We want to use quad trees to store an `N x N` boolean grid. Each cell in the grid
can only be true or false. The root node represents the whole grid. For each node, it will
be subdivided into four children nodes until the values in the region it represents
are all the same.

Each node has another two boolean attributes : `isLeaf` and `val`.
`isLeaf` is true if and only if the node is a leaf node. The `val`
attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you
understand the problem better:

Given the `8 x 8` grid below, we want to construct the corresponding quad tree:

It can be divided according to the definition above:

The corresponding quad tree should be as following, where each node is represented as a
`(isLeaf, val)` pair.

For the non-leaf nodes, `val` can be arbitrary, so it is represented as
`*`.

Note:

`N` is less than `1000` and guaranteened to be a power of 2.

If you want to know more about the quad tree, you can refer to its wiki.

【中文翻译】
我们需要使用四叉树来存储 N×N 的布尔网格。网格中的每个单元格只能是 true 或 false。
根节点表示整个网格。对于每个节点，它将被细分为四个子节点，直到它所代表的区域内所有值都相同。

每个节点有两个布尔属性：isLeaf 和 val。isLeaf 为 true 当且仅当该节点是叶子节点。
叶子节点的 val 属性包含其代表区域的值。

任务是使用四叉树表示给定的网格。

注意：
    N 小于 1000 且保证是 2 的幂。
    如果想知道更多关于四叉树的信息，可以参考其维基页面。
"""

from typing import List, Optional


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def build(r: int, c: int, size: int) -> Node:
            if size == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            half = size // 2
            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)

            # If all four children are leaves with the same value, merge
            if (topLeft.isLeaf and topRight.isLeaf and
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, len(grid))


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归分治。从整个 N×N 网格开始：
# 1. 如果网格大小为 1，直接创建叶子节点，值为 grid[r][c] == 1
# 2. 否则将当前区域平分为四个等大的子区域（左上、右上、左下、右下），递归构建
# 3. 递归返回后检查四个子节点：如果它们都是叶子节点且值相同，则可将当前节点合并为一个
#    叶子节点（优化：避免不必要的细分）
# 4. 否则当前节点为非叶子节点，四个子节点为刚刚递归构建的节点
#
# 时间复杂度: O(N^2) — 需要访问每个单元格。T(N) = 4*T(N/4) + O(1)，但合并检查也需
#              遍历子节点。总体每个单元格在递归树中只被处理常数次。
# 空间复杂度: O(log N) — 递归调用栈深度（因为像二分一样每次减半）
#
# 关键点:
# - 分治递归，每次将网格分成四个象限
# - 合并优化：当四个子区域值相同时合并为一个叶子节点
# - 注意 base case：size == 1 时直接返回叶子节点
