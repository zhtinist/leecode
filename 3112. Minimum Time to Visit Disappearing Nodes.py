"""
LeetCode #3112 - Minimum Time to Visit Disappearing Nodes
访问消失节点的最少时间
https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/

给你一个二维数组 `edges` 表示一个 `n` 个点的无向图，其中 `edges[i] = [u_i, v_i, length_i]` 表示节点 `u_i` 和节点 `v_i` 之间有一条需要 `length_i` 单位时间通过的无向边。
同时给你一个数组 `disappear` ，其中 `disappear[i]` 表示节点 `i` 从图中消失的时间点，在那一刻及以后，你无法再访问这个节点。
注意，图有可能一开始是不连通的，两个节点之间也可能有多条边。
请你返回数组 `answer` ，`answer[i]` 表示从节点 `0` 到节点 `i` 需要的 最少 单位时间。如果从节点 `0` 出发 无法 到达节点 `i` ，那么 `answer[i]` 为 `-1` 。

示例 1：

输入：n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]
输出：[0,-1,4]
解释：
我们从节点 0 出发，目的是用最少的时间在其他节点消失之前到达它们。
对于节点 0 ，我们不需要任何时间，因为它就是我们的起点。
对于节点 1 ，我们需要至少 2 单位时间，通过 `edges[0]` 到达。但当我们到达的时候，它已经消失了，所以我们无法到达它。
对于节点 2 ，我们需要至少 4 单位时间，通过 `edges[2]` 到达。
示例 2：

输入：n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]
输出：[0,2,3]
解释：
我们从节点 0 出发，目的是用最少的时间在其他节点消失之前到达它们。
对于节点 0 ，我们不需要任何时间，因为它就是我们的起点。
对于节点 1 ，我们需要至少 2 单位时间，通过 `edges[0]` 到达。
对于节点 2 ，我们需要至少 3 单位时间，通过 `edges[0]` 和 `edges[1]` 到达。
示例 3：

输入：n = 2, edges = [[0,1,1]], disappear = [1,1]
输出：[0,-1]
解释：
当我们到达节点 1 的时候，它恰好消失，所以我们无法到达节点 1 。

提示：
`1 <= n <= 5 * 10^4`
`0 <= edges.length <= 10^5`
`edges[i] == [u_i, v_i, length_i]`
`0 <= u_i, v_i <= n - 1`
`1 <= length_i <= 10^5`
`disappear.length == n`
`1 <= disappear[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        import heapq
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [-1] * n
        dist[0] = 0
        pq = [(0, 0)]  # (time, node)

        while pq:
            t, u = heapq.heappop(pq)
            if t > dist[u]:
                continue
            for v, w in graph[u]:
                nt = t + w
                if nt < disappear[v] and (dist[v] == -1 or nt < dist[v]):
                    dist[v] = nt
                    heapq.heappush(pq, (nt, v))

        return dist



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Graph, Array, Shortest Path, Heap (Priority Queue)
#
# 解题思路:
# 使用Dijkstra最短路径算法，从节点0开始。在松弛每条边时，
# 额外检查到达目标节点的时间是否小于该节点的消失时间disappear[v]。
# 只有到达时间严格小于消失时间时，才能访问该节点并更新距离。
# 如果无法到达（距离仍为-1），保持-1。
#
# 时间复杂度: O((V+E) log V)
# 空间复杂度: O(V+E)
#
# 关键点:
# - Dijkstra中加入消失时间约束
# - 到达时间必须严格小于disappear[v]
# - 重边不影响（Dijkstra自动取最短）
