"""
LeetCode #684 - Redundant Connection
中文题名：冗余连接
https://leetcode.com/problems/redundant-connection/

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2,
..., N), with one additional edge added. The added edge has two different vertices chosen
from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `edges`. Each element of `edges`
is a pair `[u, v]` with `u Update (2017-09-26):

We have overhauled the problem description + test cases and specified clearly the graph is
an undirected graph. For the directed graph follow up please see
Redundant
Connection II). We apologize for any inconvenience caused.

【中文翻译】
在本题中，树指的是一个连通且无环的无向图。

给定输入是一个有 N 个节点（1 到 N 各不相同的值）的图，它原本是一棵树，但添加了一条额外的边。添加的这条边的两个顶点选自 1 到 N，且这条边在原本的树中不存在。

结果图以二维数组 `edges` 的形式给出。`edges` 中的每个元素是一对 `[u, v]`，其中 u < v，表示连接 u 和 v 的一条无向边。

返回一条可以删除的边，使得结果图变成一棵有 N 个节点的树。如果有多个答案，则返回 `edges` 中最后出现的那条边。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图如下：
  1
 / \
2 - 3

示例 2：

输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图如下：
5 - 1 - 2
    |   |
    4 - 3

注意：

输入的二维数组大小在 3 到 1000 之间。

二维数组中的整数在 1 到 N 之间，其中 N 是输入数组的大小。
"""

from typing import List, Optional


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True

        result = []
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):
                result = [u, v]
        return result









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用并查集（Union-Find）检测图中成环的边。
# 遍历每条边 [u, v]：
# - 如果 u 和 v 已经在同一个集合中（find(u) == find(v)），说明添加这条边会形成环，
#   这条边就是冗余边，直接返回。
# - 否则，将 u 和 v 合并到同一个集合中。
# 由于题目保证存在一条冗余边且要求返回 edges 中最后出现的，按顺序遍历并返回第一个
# 导致环的边即可（因为之后图已经不连通，但题目只要求删除最后出现的冗余边）。
# 注意：需要返回 edges 中最后出现的那条冗余边，因此需遍历完所有边。
#
# 时间复杂度: O(N * α(N)) ≈ O(N) - α 为阿克曼函数的反函数，近似常数
# 空间复杂度: O(N) - 并查集存储 N 个节点的父节点
#
# 关键点:
# - 并查集的 find + path compression
# - union 返回是否成功合并（是否形成环）
# - 需要返回最后一条导致环的边（遍历完所有边）
