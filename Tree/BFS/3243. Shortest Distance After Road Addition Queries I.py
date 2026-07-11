"""
LeetCode #3243 - Shortest Distance After Road Addition Queries I
新增道路查询后的最短距离 I
https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/

给你一个整数 `n` 和一个二维整数数组 `queries`。
有 `n` 个城市，编号从 `0` 到 `n - 1`。初始时，每个城市 `i` 都有一条单向道路通往城市 `i + 1`（ `0 <= i < n - 1`）。
`queries[i] = [u_i, v_i]` 表示新建一条从城市 `u_i` 到城市 `v_i` 的单向道路。每次查询后，你需要找到从城市 `0` 到城市 `n - 1` 的最短路径的长度。
返回一个数组 `answer`，对于范围 `[0, queries.length - 1]` 中的每个 `i`，`answer[i]` 是处理完前 `i + 1` 个查询后，从城市 `0` 到城市 `n - 1` 的最短路径的长度。

示例 1：

输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]
输出： [3, 2, 1]
解释：

新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。

新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。

新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。
示例 2：

输入： n = 4, queries = [[0, 3], [0, 2]]
输出： [1, 1]
解释：

新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。

新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。

提示：
`3 <= n <= 500`
`1 <= queries.length <= 500`
`queries[i].length == 2`
`0 <= queries[i][0] < queries[i][1] < n`
`1 < queries[i][1] - queries[i][0]`
查询中没有重复的道路。
"""

from typing import List, Optional


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        from collections import deque
        # 邻接表
        graph = {i: [i + 1] for i in range(n - 1)}
        graph[n - 1] = []

        def bfs() -> int:
            q = deque([0])
            dist = [-1] * n
            dist[0] = 0
            while q:
                u = q.popleft()
                if u == n - 1:
                    return dist[u]
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return -1

        ans = []
        for u, v in queries:
            graph[u].append(v)
            ans.append(bfs())

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Breadth-First Search, Graph, Array
#
# 解题思路:
# 每次添加新道路后，使用 BFS 求从城市 0 到城市 n-1 的最短路径。
# n <= 500，queries <= 500，BFS 每次 O(n + edges) 可接受。
# 初始图中每个城市有一条到下一个城市的单向道路。
# 每次查询添加一条新边后重新 BFS。
#
# 时间复杂度: O(q * (n + q)) — q 次 BFS，每次 O(n + edges)
# 空间复杂度: O(n + q)
#
# 关键点:
# - 小数据量允许每轮都重新 BFS
# - 基础道路 i → i+1 保证图始终连通
