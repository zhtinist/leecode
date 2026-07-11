"""
LeetCode #2146 - K Highest Ranked Items Within a Price Range
价格范围内最高排名的 K 样物品
https://leetcode.cn/problems/k-highest-ranked-items-within-a-price-range/

给你一个下标从 0 开始的二维整数数组 `grid` ，它的大小为 `m x n` ，表示一个商店中物品的分布图。数组中的整数含义为：
`0` 表示无法穿越的一堵墙。
`1` 表示可以自由通过的一个空格子。
所有其他正整数表示该格子内的一样物品的价格。你可以自由经过这些格子。
从一个格子走到上下左右相邻格子花费 `1` 步。
同时给你一个整数数组 `pricing` 和 `start` ，其中 `pricing = [low, high]` 且 `start = [row, col]` ，表示你开始位置为 `(row, col)` ，同时你只对物品价格在 闭区间 `[low, high]` 之内的物品感兴趣。同时给你一个整数 `k` 。
你想知道给定范围 内 且 排名最高 的 `k` 件物品的 位置 。排名按照优先级从高到低的以下规则制定：
距离：定义为从 `start` 到一件物品的最短路径需要的步数（较近 距离的排名更高）。
价格：较低 价格的物品有更高优先级，但只考虑在给定范围之内的价格。
行坐标：较小 行坐标的有更高优先级。
列坐标：较小 列坐标的有更高优先级。
请你返回给定价格内排名最高的 `k` 件物品的坐标，将它们按照排名排序后返回。如果给定价格内少于 `k` 件物品，那么请将它们的坐标 全部 返回。

示例 1：

输入：grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3 输出：[[0,1],[1,1],[2,1]] 解释：起点为 (0,0) 。 价格范围为 [2,5] ，我们可以选择的物品坐标为 (0,1)，(1,1)，(2,1) 和 (2,2) 。 这些物品的排名为： - (0,1) 距离为 1 - (1,1) 距离为 2 - (2,1) 距离为 3 - (2,2) 距离为 4 所以，给定价格范围内排名最高的 3 件物品的坐标为 (0,1)，(1,1) 和 (2,1) 。
示例 2：

输入：grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2 输出：[[2,1],[1,2]] 解释：起点为 (2,3) 。 价格范围为 [2,3] ，我们可以选择的物品坐标为 (0,1)，(1,1)，(1,2) 和 (2,1) 。 这些物品的排名为：  - (2,1) 距离为 2 ，价格为 2 - (1,2) 距离为 2 ，价格为 3 - (1,1) 距离为 3 - (0,1) 距离为 4 所以，给定价格范围内排名最高的 2 件物品的坐标为 (2,1) 和 (1,2) 。
示例 3：

输入：grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3 输出：[[2,1],[2,0]] 解释：起点为 (0,0) 。 价格范围为 [2,3] ，我们可以选择的物品坐标为 (2,0) 和 (2,1) 。 这些物品的排名为： - (2,1) 距离为 5 - (2,0) 距离为 6 所以，给定价格范围内排名最高的 2 件物品的坐标为 (2,1) 和 (2,0) 。 注意，k = 3 但给定价格范围内只有 2 件物品。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 10^5`
`1 <= m * n <= 10^5`
`0 <= grid[i][j] <= 10^5`
`pricing.length == 2`
`2 <= low <= high <= 10^5`
`start.length == 2`
`0 <= row <= m - 1`
`0 <= col <= n - 1`
`grid[row][col] > 0`
`1 <= k <= m * n`
"""

from typing import List, Optional


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start

        from collections import deque
        queue = deque([(sr, sc, 0)])
        visited = {(sr, sc)}
        candidates = []

        # BFS
        while queue:
            r, c, dist = queue.popleft()
            price = grid[r][c]
            if price >= 2 and low <= price <= high:
                candidates.append((dist, price, r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] != 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        candidates.sort()
        return [[r, c] for _, _, r, c in candidates[:k]]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Breadth-First Search, Array, Matrix, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 使用 BFS 从起点开始逐层遍历网格。BFS 天然保证了访问顺序按距离递增，因此不需要额外按
# 距离排序后再按价格/行列排序。对于每个访问到的格子，如果其价格在 [low, high] 范围内
# 且 >= 2（即不是空格子/墙），将其加入候选列表，记录 (距离, 价格, 行, 列)。
# 遍历完成后，对所有候选项按多关键字排序，取前 k 个返回坐标。
#
# 时间复杂度: O(M*N log(M*N))，BFS 遍历所有格子 O(M*N)，排序候选 O(C log C)，
# 最坏情况 C = O(M*N)。
# 空间复杂度: O(M*N)，用于 visited 集合、队列和候选列表。
#
# 关键点:
# - BFS 保证按距离递增遍历，队列中的元素天然按距离排序
# - 多关键字排序：距离 -> 价格 -> 行 -> 列，直接使用元组排序即可
# - 障碍物 (0) 不可穿过；空格子 (1) 可穿过但不计入候选
