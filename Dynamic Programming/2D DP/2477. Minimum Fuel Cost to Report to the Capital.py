"""
LeetCode #2477 - Minimum Fuel Cost to Report to the Capital
到达首都的最少油耗
https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/

给你一棵 `n` 个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从 `0` 到 `n - 1` ，且恰好有 `n - 1` 条路。`0` 是首都。给你一个二维整数数组 `roads` ，其中 `roads[i] = [a_i, b_i]` ，表示城市 `a_i` 和 `b_i` 之间有一条 双向路 。
每个城市里有一个代表，他们都要去首都参加一个会议。
每座城市里有一辆车。给你一个整数 `seats` 表示每辆车里面座位的数目。
城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。
请你返回到达首都最少需要多少升汽油。

示例 1：

输入：roads = [[0,1],[0,2],[0,3]], seats = 5 输出：3 解释： - 代表 1 直接到达首都，消耗 1 升汽油。 - 代表 2 直接到达首都，消耗 1 升汽油。 - 代表 3 直接到达首都，消耗 1 升汽油。 最少消耗 3 升汽油。
示例 2：

输入：roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2 输出：7 解释： - 代表 2 到达城市 3 ，消耗 1 升汽油。 - 代表 2 和代表 3 一起到达城市 1 ，消耗 1 升汽油。 - 代表 2 和代表 3 一起到达首都，消耗 1 升汽油。 - 代表 1 直接到达首都，消耗 1 升汽油。 - 代表 5 直接到达首都，消耗 1 升汽油。 - 代表 6 到达城市 4 ，消耗 1 升汽油。 - 代表 4 和代表 6 一起到达首都，消耗 1 升汽油。 最少消耗 7 升汽油。
示例 3：

输入：roads = [], seats = 1 输出：0 解释：没有代表需要从别的城市到达首都。

提示：
`1 <= n <= 10^5`
`roads.length == n - 1`
`roads[i].length == 2`
`0 <= a_i, b_i < n`
`a_i != b_i`
`roads` 表示一棵合法的树。
`1 <= seats <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        total_fuel = 0

        def dfs(node: int, parent: int) -> int:
            nonlocal total_fuel
            people = 1  # this node has 1 person
            for neighbor in graph[node]:
                if neighbor != parent:
                    people += dfs(neighbor, node)
            # Number of cars needed to go from this node to parent
            if node != 0:
                cars = (people + seats - 1) // seats  # ceil(people / seats)
                total_fuel += cars
            return people

        dfs(0, -1)
        return total_fuel

# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Breadth-First Search, Graph
#
# 解题思路:
# 这是一道树形 DP 问题。首都为根节点 0，所有代表需要前往首都。
# 使用 DFS 自底向上计算每个子树中的人数（people）。
# 从节点 u 到其父节点需要 ceil(people / seats) 辆车，每辆车消耗 1 升汽油。
# 累加所有边上的车辆数即为总油耗。
#
# 时间复杂度: O(n)，每个节点和边访问一次
# 空间复杂度: O(n)，邻接表和递归栈
#
# 关键点:
# - 自底向上的 DFS 计算子树人数
# - 向上取整：(people + seats - 1) // seats
# - 首都节点（0）不需要向上移动，不计油耗
