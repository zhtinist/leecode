"""
LeetCode #429 - N-ary Tree Level Order Traversal
中文题名：N叉树的层序遍历
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from
left to right, level by level).

For example, given a `3-ary` tree:

We should return its level order traversal:

[
[1],
[3,2,4],
[5,6]
]

Note:

The depth of the tree is at most `1000`.

The total number of nodes is at most `5000`.

【中文翻译】
给定一个 N 叉树，返回其节点值的层序遍历（即从左到右，逐层遍历）。

例如，给定一个 3 叉树：
    返回其层序遍历结果：
    [
        [1],
        [3,2,4],
        [5,6]
    ]

注意：
    树的深度最多为 1000。
    节点总数最多为 5000。
"""

from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_vals = []

            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                for child in node.children:
                    queue.append(child)

            result.append(level_vals)

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS（广度优先搜索）进行层序遍历。
# 1. 使用队列存储待访问节点，初始将根节点入队
# 2. 每轮处理队列中当前层的所有节点（记录 level_size）
# 3. 对当前层的每个节点：取出、记录值、将其所有子节点入队
# 4. 当队列为空时遍历结束
#
# 与二叉树层序遍历唯一的不同在于：这里每个节点的子节点是一个列表（children），
# 需要遍历所有子节点将其入队，而不是仅左右两个子节点。
#
# 时间复杂度: O(N) — 每个节点访问一次
# 空间复杂度: O(N) — 队列在最坏情况下存储一层所有节点（最底层可能接近 N）
#
# 关键点:
# - BFS + 队列是层序遍历的标准解法
# - 通过 level_size 控制逐层输出
# - 将 children 列表中的每个子节点入队
