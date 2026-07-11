"""
LeetCode #2101 - Detonate the Maximum Bombs
引爆最多的炸弹
https://leetcode.cn/problems/detonate-the-maximum-bombs/

给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。
炸弹用一个下标从 0 开始的二维整数数组 `bombs` 表示，其中 `bombs[i] = [x_i, y_i, r_i]` 。`x_i` 和 `y_i` 表示第 `i` 个炸弹的 X 和 Y 坐标，`r_i` 表示爆炸范围的 半径 。
你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。
给你数组 `bombs` ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。

示例 1：

输入：bombs = [[2,1,3],[6,1,4]] 输出：2 解释： 上图展示了 2 个炸弹的位置和爆炸范围。 如果我们引爆左边的炸弹，右边的炸弹不会被影响。 但如果我们引爆右边的炸弹，两个炸弹都会爆炸。 所以最多能引爆的炸弹数目是 max(1, 2) = 2 。
示例 2：

输入：bombs = [[1,1,5],[10,10,5]] 输出：1 解释： 引爆任意一个炸弹都不会引爆另一个炸弹。所以最多能引爆的炸弹数目为 1 。
示例 3：

输入：bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]] 输出：5 解释： 最佳引爆炸弹为炸弹 0 ，因为： - 炸弹 0 引爆炸弹 1 和 2 。红色圆表示炸弹 0 的爆炸范围。 - 炸弹 2 引爆炸弹 3 。蓝色圆表示炸弹 2 的爆炸范围。 - 炸弹 3 引爆炸弹 4 。绿色圆表示炸弹 3 的爆炸范围。 所以总共有 5 个炸弹被引爆。

提示：
`1 <= bombs.length <= 100`
`bombs[i].length == 3`
`1 <= x_i, y_i, r_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                dx = xi - xj
                dy = yi - yj
                if dx * dx + dy * dy <= ri * ri:
                    graph[i].append(j)

        def dfs(node, visited):
            visited.add(node)
            count = 1
            for nxt in graph[node]:
                if nxt not in visited:
                    count += dfs(nxt, visited)
            return count

        max_count = 0
        for i in range(n):
            max_count = max(max_count, dfs(i, set()))

        return max_count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Graph, Geometry, Array, Math
#
# 解题思路:
# 将炸弹列表建模为有向图：如果炸弹i的爆炸范围能够覆盖炸弹j（两点距离 <= 炸弹i的半径），
# 则存在一条从i到j的有向边。对每个炸弹为起点运行DFS，计算从该炸弹出发能引爆的最大数量，
# 取所有起点的最大值。
# 距离判断使用平方比较 (dx*dx + dy*dy <= ri*ri)，避免浮点数开方带来的精度误差。
#
# 时间复杂度: O(N^3) 最坏情况，其中N为炸弹数量（N<=100）。
# 建图 O(N^2)，对每个节点DFS O(N+E)=O(N^2)，综合 O(N^3) 在 N<=100 时完全可接受。
# 空间复杂度: O(N^2)，邻接表存储图。
#
# 关键点:
# - 使用平方距离比较，避免浮点精度问题。
# - DFS/BFS均可，每个起点独立搜索（visited集合每次重新初始化）。
# - 有向图的边方向：bomb i -> bomb j 当且仅当 i 能引爆 j（单向）。
