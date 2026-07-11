"""
LeetCode #1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
中文题名：阈值距离内邻居最少的城市
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

There are `n` cities numbered from `0` to `n-1`.
Given the array `edges` where `edges[i] = [fromi,
toi, weighti]` represents a bidirectional and weighted
edge between cities `fromi` and `toi`,
and given the integer `distanceThreshold`.

Return the city with the smallest number of cities that are
reachable through some path and whose distance is at most `distanceThreshold`,
If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and
j is equal to the sum of the edges' weights along that
path.

Example 1:

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.

Constraints:

`2 <= n <= 100`

`1 <= edges.length <= n * (n - 1) / 2`

`edges[i].length == 3`

`0 <= fromi < toi < n`

`1 <= weighti, distanceThreshold <= 10^4`

All pairs `(fromi, toi)` are distinct.

【中文翻译】
有 n 个城市，编号从 0 到 n-1。给定数组 edges，其中 edges[i] = [fromi, toi, weighti]
表示城市 fromi 和 toi 之间的一条双向加权边。同时给定整数 distanceThreshold。

返回在距离阈值 distanceThreshold 以内可到达城市数量最少的城市。
如果有多个这样的城市，返回编号最大的城市。

注意，连接城市 i 和 j 的路径的距离等于该路径上所有边的权重之和。

示例 1：

输入: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
输出: 3
解释: 上图描述了该图。
每个城市在 distanceThreshold=4 内的邻居城市：
城市 0 -> [城市 1, 城市 2]
城市 1 -> [城市 0, 城市 2, 城市 3]
城市 2 -> [城市 0, 城市 1, 城市 3]
城市 3 -> [城市 1, 城市 2]
城市 0 和 3 在 distanceThreshold=4 内都有 2 个邻居城市，但应返回编号最大的城市 3。

示例 2：

输入: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
输出: 0
解释: 上图描述了该图（此处省略插图）。
每个城市在 distanceThreshold=2 内的邻居城市：
城市 0 -> [城市 1]
城市 1 -> [城市 0, 城市 4]
城市 2 -> [城市 3, 城市 4]
城市 3 -> [城市 2, 城市 4]
城市 4 -> [城市 1, 城市 2, 城市 3]
城市 0 只有 1 个邻居城市在 distanceThreshold=2 以内。

约束条件：

`2 <= n <= 100`

`1 <= edges.length <= n * (n - 1) / 2`

`edges[i].length == 3`

`0 <= fromi < toi < n`

`1 <= weighti, distanceThreshold <= 10^4`

所有 (fromi, toi) 对互不相同。
"""

from typing import List, Optional


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # 初始化距离矩阵，使用一个足够大的数表示无穷远
        INF = 10 ** 9
        dist = [[INF] * n for _ in range(n)]

        # 自己到自己的距离为 0
        for i in range(n):
            dist[i][i] = 0

        # 填入已知边权
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall 全源最短路径算法
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # 统计每个城市在阈值内的可达城市数
        min_count = n
        result_city = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            # 更新：优先选 count 小的；相同时选编号大的
            if count <= min_count:
                min_count = count
                result_city = i

        return result_city



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 使用 Floyd-Warshall 算法计算所有城市对之间的最短路径距离。
#    - 初始化距离矩阵 dist[i][j]：自己到自己为 0，有直接边的设为边权，其余为无穷大。
#    - 三重循环：以每个城市 k 作为中间点，尝试松弛 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])。
# 2. Floyd-Warshall 完成后，对于每个城市 i，统计满足 dist[i][j] <= distanceThreshold 且 i != j 的城市 j 的数量。
# 3. 选择可达邻居数量最少的城市；如果有并列，选择编号最大的城市。
#
# 时间复杂度: O(N^3) — Floyd-Warshall 三重循环，n <= 100 可行
# 空间复杂度: O(N^2) — 存储 N*N 的距离矩阵
#
# 关键点:
# - Floyd-Warshall 适用于 n <= 100 的全源最短路径计算
# - 注意处理并列情况：选择编号最大的城市
# - 初始化 INF 需要足够大，避免加法溢出










