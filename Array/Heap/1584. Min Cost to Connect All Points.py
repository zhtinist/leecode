"""
LeetCode #1584 - Min Cost to Connect All Points
中文题名：连接所有点的最小费用
https://leetcode.com/problems/min-cost-to-connect-all-points/


You are given an array `points` representing integer
coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and
`[xj, yj]` is the manhattan
distance between them: `|xi - xj| +
|yi - yj|`, where `|val|` denotes the
absolute value of `val`.

Return the minimum cost to make all points connected. All points are
connected if there is exactly one simple path between any two
points.

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4

Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000

Example 5:

Input: points = [[0,0]]
Output: 0

Constraints:

`1 <= points.length <= 1000`

`-106 <= xi, yi <=
106`

All pairs `(xi, yi)` are distinct.

【中文翻译】
给定平面上的点数组 points，其中 points[i] = [xi, yi]。
连接两点 [xi, yi] 和 [xj, yj] 的费用为曼哈顿距离 |xi-xj| + |yi-yj|。
返回连接所有点的最小总费用。

示例 1：输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20

示例 2：输入：points = [[3,12],[-2,5],[-4,1]]
输出：18
"""

from typing import List, Optional
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        heap = [(0, 0)]
        total_cost = 0
        visited_count = 0
        while visited_count < n:
            dist, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            visited_count += 1
            total_cost += dist
            for v in range(n):
                if not visited[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if d < min_dist[v]:
                        min_dist[v] = d
                        heapq.heappush(heap, (d, v))
        return total_cost



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 最小生成树（MST）问题。使用 Prim 算法：从任意点开始，维护已连接集合到未连接点的最短距离。
# 每次选择距离最小的未连接点加入集合，更新与该点相邻的未连接点的距离。
# 完全图（任意两点可连），直接计算所有点对距离。
#
# 时间复杂度: O(N^2) — Prim 算法，每轮扫描所有未访问点
# 空间复杂度: O(N) — visited 和 min_dist 数组
#
# 关键点:
# - 最小生成树问题
# - 曼哈顿距离作为边权重
# - Prim 算法在稠密图中优于 Kruskal












