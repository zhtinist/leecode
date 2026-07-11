"""
LeetCode #1976 - Number of Ways to Arrive at Destination
到达目的地的方案数
https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/

你在一个城市里，城市由 `n` 个路口组成，路口编号为 `0` 到 `n - 1` ，某些路口之间有 双向 道路。输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。
给你一个整数 `n` 和二维整数数组 `roads` ，其中 `roads[i] = [u_i, v_i, time_i]` 表示在路口 `u_i` 和 `v_i` 之间有一条需要花费 `time_i` 时间才能通过的道路。你想知道花费 最少时间 从路口 `0` 出发到达路口 `n - 1` 的方案数。
请返回花费 最少时间 到达目的地的 路径数目 。由于答案可能很大，将结果对 `10^9 + 7` 取余 后返回。

示例 1：
输入：n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]] 输出：4 解释：从路口 0 出发到路口 6 花费的最少时间是 7 分钟。 四条花费 7 分钟的路径分别为： - 0 ➝ 6 - 0 ➝ 4 ➝ 6 - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6 - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
示例 2：
输入：n = 2, roads = [[1,0,10]] 输出：1 解释：只有一条从路口 0 到路口 1 的路，花费 10 分钟。

提示：
`1 <= n <= 200`
`n - 1 <= roads.length <= n * (n - 1) / 2`
`roads[i].length == 3`
`0 <= u_i, v_i <= n - 1`
`1 <= time_i <= 10^9`
`u_i != v_i`
任意两个路口之间至多有一条路。
从任意路口出发，你能够到达其他任意路口。
"""

from typing import List, Optional


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Dijkstra's algorithm with path counting.
        dist[i] = shortest distance to node i.
        ways[i] = number of ways to reach node i with shortest distance.
        """
        import heapq

        MOD = 10**9 + 7

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float("inf")] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_dist, v))
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Graph, Topological Sort, Dynamic Programming, Shortest Path
#
# 解题思路:
# 使用 Dijkstra 算法求最短路径，同时统计最短路径的数量。
# dist[i] = 从 0 到 i 的最短距离
# ways[i] = 从 0 到 i 的最短路径数量
# 松弛操作时：
# - 如果新距离 < dist[v]：更新 dist[v]，ways[v] = ways[u]
# - 如果新距离 == dist[v]：ways[v] += ways[u]
# 最终返回 ways[n-1] % MOD。
#
# 时间复杂度: O((N + E) log N)，Dijkstra 算法
# 空间复杂度: O(N + E)，图和辅助数组
#
# 关键点:
# - 在 Dijkstra 松弛过程中同时统计路径数
# - 距离相等时累加路径数
# - 需要取模 10^9+7
