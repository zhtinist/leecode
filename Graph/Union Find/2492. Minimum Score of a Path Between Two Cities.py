"""
LeetCode #2492 - Minimum Score of a Path Between Two Cities
两个城市间路径的最小分数
https://leetcode.cn/problems/minimum-score-of-a-path-between-two-cities/

给你一个正整数 `n` ，表示总共有 `n` 个城市，城市从 `1` 到 `n` 编号。给你一个二维数组 `roads` ，其中 `roads[i] = [a_i, b_i, distance_i]` 表示城市 `a_i` 和 `b_i` 之间有一条 双向 道路，道路距离为 `distance_i` 。城市构成的图不一定是连通的。
两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。
返回城市 `1` 和城市 `n` 之间的所有路径的 最小 分数。
注意：
一条路径指的是两个城市之间的道路序列。
一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 `1` 和城市 `n` 。
测试数据保证城市 `1` 和城市`n` 之间 至少 有一条路径。

示例 1：

输入：n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]] 输出：5 解释：城市 1 到城市 4 的路径中，分数最小的一条为：1 -> 2 -> 4 。这条路径的分数是 min(9,5) = 5 。 不存在分数更小的路径。
示例 2：

输入：n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]] 输出：2 解释：城市 1 到城市 4 分数最小的路径是：1 -> 2 -> 1 -> 3 -> 4 。这条路径的分数是 min(2,2,4,7) = 2 。

提示：
`2 <= n <= 10^5`
`1 <= roads.length <= 10^5`
`roads[i].length == 3`
`1 <= a_i, b_i <= n`
`a_i != b_i`
`1 <= distance_i <= 10^4`
不会有重复的边。
城市 `1` 和城市 `n` 之间至少有一条路径。
"""

from typing import List, Optional


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        BFS/DFS 遍历连通分量：
        - 因为可以重复访问节点和边，所以从城市 1 出发能到达的所有节点构成一个连通分量
        - 该连通分量中的所有边都可以出现在某条从 1 到 n 的路径上
        - 答案就是该连通分量中边权的最小值
        """
        from collections import deque

        # 构建邻接表
        graph = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        ans = float('inf')
        q = deque([1])
        visited[1] = True

        while q:
            u = q.popleft()
            for v, w in graph[u]:
                ans = min(ans, w)  # 更新遇到的最小边权
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Union Find, Graph
#
# 解题思路:
# 题目允许在路径中重复访问节点和边，因此只要某条边属于城市 1 所在的连通分量，
# 就可以构造出经过该边且从城市 1 到达城市 n 的路径。问题转化为：在包含城市 1
# 和城市 n 的连通分量中，找到边权的最小值。使用 BFS（或 DFS）从城市 1 开始遍历
# 所有可达节点，遍历过程中记录遇到的最小边权即可。
#
# 时间复杂度: O(n + m) — 其中 n 是城市数，m 是道路数，每个节点和每条边最多访问一次
# 空间复杂度: O(n + m) — 邻接表存储图结构
#
# 关键点:
# - 由于可以无限次回溯和重复经过边，整个连通分量的所有边都可达
# - 不需要找特定的"最短路径"，只需在 BFS/DFS 过程中追踪最小边权
# - 题目保证城市 1 和城市 n 之间至少有一条路径
# - 也可以用并查集（Union Find）实现，思路相同
