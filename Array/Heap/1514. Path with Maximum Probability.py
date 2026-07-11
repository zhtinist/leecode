"""
LeetCode #1514 - Path with Maximum Probability
中文题名：概率最大的路径
https://leetcode.com/problems/path-with-maximum-probability/

You are given an undirected weighted graph of `n` nodes (0-indexed),
represented by an edge list where `edges[i] = [a, b]` is an
undirected edge connecting the nodes `a` and `b` with
a probability of success of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`, find the path
with the maximum probability of success to go from `start` to `end` and
return its success probability.

If there is no path from `start` to `end`, return 0.
Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:

`2 <= n <= 10^4`

`0 <= start, end < n`

`start != end`

`0 <= a, b < n`

`a != b`

`0 <= succProb.length == edges.length <= 2*10^4`

`0 <= succProb[i] <= 1`

There is at most one edge between every two nodes.

【中文翻译】
给定一个包含 n 个节点（0 索引）的无向加权图，由边列表表示，
其中 edges[i] = [a, b] 是无向边，连接节点 a 和 b，成功遍历该边的概率为 succProb[i]。
给定两个节点 start 和 end，找出从 start 到 end 成功率最大的路径，并返回其成功概率。
如果不存在从 start 到 end 的路径，返回 0。

示例 1：

输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
输出：0.25000
解释：有两条路径，概率分别为 0.2 和 0.5*0.5=0.25。

示例 2：

输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
输出：0.30000

示例 3：

输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
输出：0.00000
解释：没有路径从 0 到 2。
"""

from typing import List, Optional
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        # Max-heap (store negative probability)
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        heap = [(-1.0, start_node)]

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob
            if node == end_node:
                return prob
            if prob < max_prob[node]:
                continue
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 Dijkstra 算法的变体。传统 Dijkstra 找最短路径，这里找最大概率路径。
# 使用最大堆（Python 中用负数模拟），每次取出概率最大的节点进行扩展。
# 维护 max_prob 数组记录到达每个节点的最大概率。对于每条边，新概率 = 当前概率 * 边概率。
# 如果新概率更大，则更新并入堆。提前终止：当弹出 end_node 时直接返回。
#
# 时间复杂度: O((N + E) log N) — 堆操作
# 空间复杂度: O(N + E) — 图存储和堆
#
# 关键点:
# - 将 Dijkstra 的最短路径改为最大概率路径
# - 概率相乘（而非相加），只减不增
# - Python 使用负值模拟最大堆
