"""
LeetCode #1615 - Maximal Network Rank
中文题名：最大网络秩
https://leetcode.com/problems/maximal-network-rank/

There is an infrastructure of `n` cities with some number of
`roads` connecting these cities. Each `roads[i] = [ai, bi]`
indicates that there is a bidirectional road between cities `ai`
and `bi`.

The network rank of two different cities
is defined as the total number of directly connected roads to
either city. If a road is directly connected to both cities, it is
only counted once.

The maximal network rank of the infrastructure is the maximum
network rank of all pairs of different cities.

Given the integer `n` and the array `roads`, return the
maximal network rank of the entire infrastructure.

Example 1:

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

Example 2:

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.

Example 3:

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

Constraints:

`2 <= n <= 100`

`0 <= roads.length <= n * (n - 1) / 2`

`roads[i].length == 2`

`0 <= ai, bi <= n-1`

`ai != bi`

Each pair of cities has at most one road connecting them.

【中文翻译】
给定 n 个城市和道路列表 roads，其中 roads[i] = [a, b] 表示城市 a 和 b 之间有一条双向道路。
网络秩定义为与这两个城市直接相连的道路总数（如果两个城市之间有道路，则只计算一次）。
求整个基础设施网络中任意两个不同城市之间的最大网络秩。

示例 1：
输入: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
输出: 4
解释: 城市 0 和 1 的网络秩为 4，因为共有 4 条道路连接到这两个城市中的至少一个（0连接1和3，1连接0,2,3）。
"""

from typing import List, Optional


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = set()

        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected.add((min(a, b), max(a, b)))

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if (i, j) in connected:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 计算每个城市的度数（相连道路数），并用集合记录哪些城市对之间直接相连。
# 枚举所有城市对 (i, j)，其网络秩 = degree[i] + degree[j] - (1 if 直接相连 else 0)。
# 取所有城市对中的最大值即为答案。
#
# 时间复杂度: O(N^2 + E) — 计算度数 O(E)，枚举所有城市对 O(N^2)
# 空间复杂度: O(N + E) — 存储度数和连接关系
#
# 关键点:
# - 只有两个城市直接相连时才需要减1（避免重复计算同一条道路）
# - 使用 (min, max) 元组存储无向边以统一比较
