"""
LeetCode #1786 - Number of Restricted Paths From First to Last Node
中文题名：从第一个节点到最后一个节点的受限路径数
https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

There is an undirected weighted connected graph. You are given a positive integer `n` which denotes that the graph has `n` nodes labeled from `1` to `n`, and an array `edges` where each `edges[i] = [ui, vi, weighti]` denotes that there is an edge between nodes `ui` and `vi` with weight equal to `weighti`.

A path from node `start` to node `end` is a sequence of nodes `[z0, z1, z2, ..., zk]` such that `z0 = start` and `zk = end` and there is an edge between `zi` and `zi+1` where `0 <= i <= k-1`.

The distance of a path is the sum of the weights on the edges of the path. Let `distanceToLastNode(x)` denote the shortest distance of a path between node `n` and node `x`. A restricted path is a path that also satisfies that `distanceToLastNode(zi) > distanceToLastNode(zi+1)` where `0 <= i <= k-1`.

Return the number of restricted paths from node `1` to node `n`. Since that number may be too large, return it modulo `109 + 7`.

Example 1:

Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its `distanceToLastNode value in blue. `The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

Example 2:

Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its `distanceToLastNode value in blue. `The only restricted path is 1 --> 3 --> 7.

Constraints:

`1 <= n <= 2 * 104`

`n - 1 <= edges.length <= 4 * 104`

`edges[i].length == 3`

`1 <= ui, vi <= n`

`ui != vi`

`1 <= weighti <= 105`

There is at most one edge between any two nodes.

There is at least one path between any two nodes.

【中文翻译】
给定一个带权无向图，有 n 个节点（1 到 n）。定义受限路径为：从节点 1 到节点 n 的路径，
路径上每个节点到节点 n 的最短距离严格递减。
返回到达节点 n 的受限路径数量，对 10^9+7 取模。

示例 1：
输入: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
输出: 3
解释: 受限路径有三条：1→2→5, 1→3→5, 1→4→2→5...等。
"""

from typing import List, Optional
import heapq
from collections import defaultdict


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        # 构建邻接表
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra 从 n 出发计算最短距离
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nei, w in graph[node]:
                nd = d + w
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))

        # DP/memo: 计算从 1 到 n 的受限路径数
        memo = {}

        def dfs(node: int) -> int:
            if node == n:
                return 1
            if node in memo:
                return memo[node]
            total = 0
            for nei, _ in graph[node]:
                if dist[nei] < dist[node]:
                    total = (total + dfs(nei)) % MOD
            memo[node] = total
            return total

        return dfs(1)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. Dijkstra 算法从节点 n 出发，计算所有节点到 n 的最短距离 dist。
# 2. 使用记忆化 DFS 从节点 1 开始，统计受限路径数：
#    - 对于当前节点 u，走到邻居 v 当且仅当 dist[v] < dist[u]（距离严格递减）
#    - 到达 n 时返回 1（找到一条路径）
# 3. 用 memo 避免重复计算。
#
# 时间复杂度: O(E log N) — Dijkstra + O(V+E) — DFS
# 空间复杂度: O(V + E)
#
# 关键点:
# - Dijkstra 从终点做起，得到所有节点的最短距离
# - 受限路径要求沿距离递减方向走（类似于在 DAG 上 DP）
# - memo 保证每个节点只计算一次
