"""
LeetCode #2662 - Minimum Cost of a Path With Special Roads
前往目标的最小代价
https://leetcode.cn/problems/minimum-cost-of-a-path-with-special-roads/

给你一个数组 `start` ，其中 `start = [startX, startY]` 表示你的初始位置位于二维空间上的 `(startX, startY)` 。另给你一个数组 `target` ，其中 `target = [targetX, targetY]` 表示你的目标位置 `(targetX, targetY)` 。
从位置 `(x1, y1)` 到空间中任一其他位置 `(x2, y2)` 的 代价 是 `|x2 - x1| + |y2 - y1|` 。
给你一个二维数组 `specialRoads` ，表示空间中存在的一些 特殊路径。其中 `specialRoads[i] = [x1_i, y1_i, x2_i, y2_i, cost_i]` 表示第 `i` 条特殊路径可以从 `(x1_i, y1_i)` 到 `(x2_i, y2_i)` ，但成本等于 `cost_i` 。你可以使用每条特殊路径任意次数。
返回从 `(startX, startY)` 到 `(targetX, targetY)` 所需的 最小 代价。

示例 1：

输入：start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
输出：5
解释：
(1,1) 到 (1,2) 花费为 |1 - 1| + |2 - 1| = 1。
(1,2) 到 (3,3)。使用 `specialRoads[0]` 花费为 2。
(3,3) 到 (3,4) 花费为 |3 - 3| + |4 - 3| = 1。
(3,4) 到 (4,5)。使用 `specialRoads[1]` 花费为 1。
所以总花费是 1 + 2 + 1 + 1 = 5。
示例 2：

输入：start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
输出：7
解释：
不使用任何特殊路径，直接从开始到结束位置是最优的，花费为 |5 - 3| + |7 - 2| = 7。
注意 `specialRoads[0]` 直接从 (5,7) 到 (3,2)。
示例 3：

输入：start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]
输出：8
解释：
(1,1) 到 (1,2) 花费为 |1 - 1| + |2 - 1| = 1。
(1,2) 到 (7,4)。使用 `specialRoads[1]` 花费为 4。
(7,4) 到 (10,4) 花费为 |10 - 7| + |4 - 4| = 3。

提示：
`start.length == target.length == 2`
`1 <= startX <= targetX <= 10^5`
`1 <= startY <= targetY <= 10^5`
`1 <= specialRoads.length <= 200`
`specialRoads[i].length == 5`
`startX <= x1_i, x2_i <= targetX`
`startY <= y1_i, y2_i <= targetY`
`1 <= cost_i <= 10^5`
"""

from typing import List, Optional


import heapq


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # Dijkstra on the graph of points (start, target, and special road endpoints)
        # Manhattan distance between any two points without special roads
        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        points = {}
        # assign index to each unique point
        def get_idx(pt):
            key = tuple(pt)
            if key not in points:
                points[key] = len(points)
            return points[key]

        # Collect all relevant points
        get_idx(start)
        get_idx(target)
        for x1, y1, x2, y2, cost in specialRoads:
            get_idx([x1, y1])
            get_idx([x2, y2])

        n = len(points)
        coords = [None] * n
        for pt, idx in points.items():
            coords[idx] = list(pt)

        # Build adjacency list: from each point, we can go to target directly (Manhattan)
        # or use any special road starting from this point
        dist = [float('inf')] * n
        start_idx = get_idx(start)
        target_idx = get_idx(target)
        dist[start_idx] = 0

        pq = [(0, start_idx)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == target_idx:
                return d

            # Direct Manhattan to all other points (we only need target)
            # But for completeness, try going to target directly
            direct = d + manhattan(coords[u], coords[target_idx])
            if direct < dist[target_idx]:
                dist[target_idx] = direct
                heapq.heappush(pq, (direct, target_idx))

            # Try using special roads
            for x1, y1, x2, y2, cost in specialRoads:
                # Manhattan from current to start of special road, then use road
                road_start = [x1, y1]
                road_end = [x2, y2]
                nd = d + manhattan(coords[u], road_start) + cost
                v = get_idx(road_end)
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        return dist[target_idx]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Graph, Array, Shortest Path, Heap (Priority Queue)
#
# 解题思路:
# 使用Dijkstra算法在特殊路径构成的图上求最短路径。节点包括起点、终点和所有特殊路径的端点。
# 从当前点可以沿曼哈顿距离直接走到终点，也可以先走到特殊路径起点再用特殊路径。
# 不需要对所有点对建边，而是每次出队时动态计算到各特殊路径起点的距离。
#
# 时间复杂度: O(S^2 log S) 其中S是特殊路径数量
# 空间复杂度: O(S)
#
# 关键点:
# - 节点集合是起点+终点+所有特殊路径端点
# - 边有两种：曼哈顿距离（任意两点间）和特殊路径（有向边）
# - Dijkstra动态计算曼哈顿距离避免建O(n^2)条边
