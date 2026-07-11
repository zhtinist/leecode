"""
LeetCode #2497 - Maximum Star Sum of a Graph
图中最大星和
https://leetcode.cn/problems/maximum-star-sum-of-a-graph/

给你一个 `n` 个点的无向图，节点从 `0` 到 `n - 1` 编号。给你一个长度为 `n` 下标从 0 开始的整数数组 `vals` ，其中 `vals[i]` 表示第 `i` 个节点的值。
同时给你一个二维整数数组 `edges` ，其中 `edges[i] = [a_i, b_i]` 表示节点 `a_i` 和 `b_i` 之间有一条双向边。
星图 是给定图中的一个子图，它包含一个中心节点和 `0` 个或更多个邻居。换言之，星图是给定图中一个边的子集，且这些边都有一个公共节点。
下图分别展示了有 `3` 个和 `4` 个邻居的星图，蓝色节点为中心节点。

星和 定义为星图中所有节点值的和。
给你一个整数 `k` ，请你返回 至多 包含 `k` 条边的星图中的 最大星和 。

示例 1：

输入：vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2 输出：16 解释：上图展示了输入示例。 最大星和对应的星图在上图中用蓝色标出。中心节点是 3 ，星图中还包含邻居 1 和 4 。 无法得到一个和大于 16 且边数不超过 2 的星图。
示例 2：
输入：vals = [-5], edges = [], k = 0 输出：-5 解释：只有一个星图，就是节点 0 自己。 所以我们返回 -5 。

提示：
`n == vals.length`
`1 <= n <= 10^5`
`-10^4 <= vals[i] <= 10^4`
`0 <= edges.length <= min(n * (n - 1) / 2``, 10^5)`
`edges[i].length == 2`
`0 <= a_i, b_i <= n - 1`
`a_i != b_i`
`0 <= k <= n - 1`
"""

from typing import List, Optional


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        """
        枚举每个节点作为星图中心：
        - 构建邻接表，记录每个节点的所有邻居
        - 对每个节点 i：
          收集其所有邻居的值 neighbor_vals = [vals[v] for v in graph[i]]
          按降序排序，取前 k 个正数值（只加正数才有收益）
          星图和 = vals[i] + sum(前k个正的邻居值)
        - 返回全局最大星图和
        """
        n = len(vals)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = float('-inf')
        for i in range(n):
            # 收集邻居节点的值
            neighbor_vals = [vals[neighbor] for neighbor in graph[i]]
            # 降序排序
            neighbor_vals.sort(reverse=True)
            # 取最多 k 个正的邻居值
            cur_sum = vals[i]
            for j in range(min(k, len(neighbor_vals))):
                if neighbor_vals[j] > 0:
                    cur_sum += neighbor_vals[j]
                else:
                    break
            ans = max(ans, cur_sum)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Graph, Array, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 枚举每个节点作为星图的中心。对于每个中心节点，星图可以包含它的中心节点值加上
# 至多 k 条边连接到的邻居节点。要最大化星和，应该优先选择值最大的邻居（但只选
# 正数，因为加上负数会减小总和）。实现时先构建邻接表，然后对每个节点收集其所有
# 邻居的值、按降序排序、取前 k 个正数值累加，记录全局最大值。
#
# 时间复杂度: O(n + m + n*d*log d) — m 是边数构建邻接表，d 是节点度数，
#           最坏情况下是完全图 O(n^2 log n)，但在给定约束下（m <= 10^5）可行
# 空间复杂度: O(n + m) — 邻接表存储
#
# 关键点:
# - 星图可以只包含中心节点自身（0 条边），所以答案至少是 max(vals)
# - 只加正的邻居值，负数对总和没有贡献
# - k 可能大于该节点的度数，此时取所有正的邻居值即可
# - 可以使用堆（维护前 k 个最大值）来优化，但排序足够应对本题数据规模
