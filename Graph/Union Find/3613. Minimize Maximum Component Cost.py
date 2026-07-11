"""
LeetCode #3613 - Minimize Maximum Component Cost
最小化连通分量的最大成本
https://leetcode.cn/problems/minimize-maximum-component-cost/

给你一个无向连通图，包含 `n` 个节点，节点编号从 0 到 `n - 1`，以及一个二维整数数组 `edges`，其中 `edges[i] = [u_i, v_i, w_i]` 表示一条连接节点 `u_i` 和节点 `v_i` 的无向边，边权为 `w_i`，另有一个整数 `k`。
你可以从图中移除任意数量的边，使得最终的图中 最多 只包含 `k` 个连通分量。
连通分量的 成本 定义为该分量中边权的 最大值 。如果一个连通分量没有边，则其代价为 0。
请返回在移除这些边之后，在所有连通分量之中的 最大成本 的 最小可能值 。

示例 1：

输入： n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2
输出： 4
解释：

移除节点 3 和节点 4 之间的边（权值为 6）。
最终的连通分量成本分别为 0 和 4，因此最大代价为 4。
示例 2：

输入： n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1
输出： 5
解释：

无法移除任何边，因为只允许一个连通分量（`k = 1`），图必须保持完全连通。
该连通分量的成本等于其最大边权，即 5。

提示：
`1 <= n <= 5 * 10^4`
`0 <= edges.length <= 10^5`
`edges[i].length == 3`
`0 <= u_i, v_i < n`
`1 <= w_i <= 10^6`
`1 <= k <= n`
输入图是连通图。
"""

from typing import List, Optional


class Solution:
    def minimizeMaxComponentCost(self, n: int, edges: List[List[int]], k: int) -> int:
        # If we can have n separate components (by removing all edges),
        # each component has cost 0, so max cost = 0
        if k >= n:
            return 0

        if not edges:
            return 0  # no edges, all isolated, cost 0

        # Sort unique weights for binary search
        weights = sorted(set(w for _, _, w in edges))

        def can(limit: int) -> bool:
            """
            Returns True if we can split into <= k components
            by keeping only edges with weight <= limit.
            Each component's max edge weight will then be <= limit.
            """
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            for u, v, w in edges:
                if w <= limit:
                    pu, pv = find(u), find(v)
                    if pu != pv:
                        parent[pu] = pv

            comps = sum(1 for i in range(n) if find(i) == i)
            return comps <= k

        # Binary search for minimum feasible max cost
        lo, hi = 0, len(weights) - 1
        ans = weights[-1]

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(weights[mid]):
                ans = weights[mid]
                hi = mid - 1
            else:
                lo = mid + 1

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Union Find, Graph, Binary Search, Sorting
#
# 解题思路:
# 问题本质：选择性地移除边，使连通分量数 <= k，并最小化各分量最大边权的最大值。
# 这是典型的"最小化最大值"问题，使用二分答案 + 并查集验证。
#
# 二分答案 L（允许的最大边权）：
# - 只保留权重 <= L 的边建图
# - 每个连通分量内的最大边权不会超过 L
# - 没有边的独立节点构成成本为 0 的分量
# - 若连通分量数 <= k，说明 L 可行（可以进一步移除边使分量数恰好 <= k）
#   注意：移除更多边只会增加分量数，不会减少，所以分量数 <= k 意味着
#   我们可以在当前基础上移除一些边来恰好达到 k 个分量
# - 若分量数 > k，说明需要更大的 L 以合并更多分量
#
# 时间复杂度: O((N + E) * log W * α(N)) — W 为边权种类数，二分 O(log W) 次
# 空间复杂度: O(N) — DSU 的 parent 数组
#
# 关键点:
# - 二分答案验证法：非直接模拟移除，而是选边建图
# - 注意分量数 <= k 即为可行（可移除更多边达到恰好 k 个分量）
# - k >= n 时直接返回 0（移除所有边，每个节点成本为 0）
# - 原图连通但可以通过切割分成多个分量
