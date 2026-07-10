"""
LeetCode #261 - Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

Given `n` nodes labeled from `0` to `n-1` and a list of
undirected edges (each edge is a pair of nodes), write a function to check whether these
edges make up a valid tree.

Example 1:

Input: `n = 5`, and `edges = [[0,1], [0,2], [0,3], [1,4]]`
Output: true

Example 2:

Input: `n = 5, `and `edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]`
Output: false

Note: you can assume that no duplicate edges will appear in `edges`. Since
all edges are undirected, `[0,1]` is the same as `[1,0]` and thus will
not appear together in `edges`.
"""

from typing import List, Optional


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 树的条件: 边数 = 节点数 - 1，且无环（连通）
        if len(edges) != n - 1:
            return False

        # 并查集（Union-Find）检测环
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False  # 已在同一集合，说明有环
            parent[root_x] = root_y
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 一棵有效的树需要满足两个条件：(1) 无环，(2) 全部连通。
# 对于 n 个节点，如果边数恰好为 n-1 且无环，则自动满足连通性。
# 使用并查集（Union-Find）：遍历每条边，如果两个端点已经在同一集合中则
# 说明存在环返回 False。路径压缩优化 find，按秩合并不是必须但可优化。
#
# 时间复杂度: O(n * α(n)) — α 为反阿克曼函数，近似 O(n)
# 空间复杂度: O(n) — parent 数组
#
# 关键点：
# - 先检查边数 == n-1（必要条件）
# - 并查集检测环
# - 也可以使用 DFS/BFS 检测连通性和环
