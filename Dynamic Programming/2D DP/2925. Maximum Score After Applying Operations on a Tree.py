"""
LeetCode #2925 - Maximum Score After Applying Operations on a Tree
在树上执行操作以后得到的最大分数
https://leetcode.cn/problems/maximum-score-after-applying-operations-on-a-tree/

有一棵 `n` 个节点的无向树，节点编号为 `0` 到 `n - 1` ，根节点编号为 `0` 。给你一个长度为 `n - 1` 的二维整数数组 `edges` 表示这棵树，其中 `edges[i] = [a_i, b_i]` 表示树中节点 `a_i` 和 `b_i` 有一条边。
同时给你一个长度为 `n` 下标从 0 开始的整数数组 `values` ，其中 `values[i]` 表示第 `i` 个节点的值。
一开始你的分数为 `0` ，每次操作中，你将执行：
选择节点 `i` 。
将 `values[i]` 加入你的分数。
将 `values[i]` 变为 `0` 。
如果从根节点出发，到任意叶子节点经过的路径上的节点值之和都不等于 0 ，那么我们称这棵树是 健康的 。
你可以对这棵树执行任意次操作，但要求执行完所有操作以后树是 健康的 ，请你返回你可以获得的 最大分数 。

示例 1：

输入：edges = [[0,1],[0,2],[0,3],[2,4],[4,5]], values = [5,2,5,2,1,1] 输出：11 解释：我们可以选择节点 1 ，2 ，3 ，4 和 5 。根节点的值是非 0 的。所以从根出发到任意叶子节点路径上节点值之和都不为 0 。所以树是健康的。你的得分之和为 values[1] + values[2] + values[3] + values[4] + values[5] = 11 。 11 是你对树执行任意次操作以后可以获得的最大得分之和。
示例 2：

输入：edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [20,10,9,7,4,3,5] 输出：40 解释：我们选择节点 0 ，2 ，3 和 4 。 - 从 0 到 4 的节点值之和为 10 。 - 从 0 到 3 的节点值之和为 10 。 - 从 0 到 5 的节点值之和为 3 。 - 从 0 到 6 的节点值之和为 5 。 所以树是健康的。你的得分之和为 values[0] + values[2] + values[3] + values[4] = 40 。 40 是你对树执行任意次操作以后可以获得的最大得分之和。

提示：
`2 <= n <= 2 * 10^4`
`edges.length == n - 1`
`edges[i].length == 2`
`0 <= a_i, b_i < n`
`values.length == n`
`1 <= values[i] <= 10^9`
输入保证 `edges` 构成一棵合法的树。
"""

from typing import List, Optional


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]],
                                     values: List[int]) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        INF = 10**18

        def dfs(u: int, parent: int):
            if len(g[u]) == 1 and u != 0:  # leaf
                return (INF, values[u])
            dp0 = 0  # u is zeroed: children must be healthy
            for v in g[u]:
                if v == parent:
                    continue
                child0, child1 = dfs(v, u)
                dp0 += min(child0, child1)
            dp1 = values[u]  # u is kept: all children can be zeroed
            return (dp0, dp1)

        total = sum(values)
        keep0, keep1 = dfs(0, -1)
        min_keep = min(keep0, keep1)
        return total - min_keep



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Dynamic Programming
#
# 解题思路:
# 树健康的条件是每条根到叶子的路径至少有一个非零节点。等价于：我们保留一些节点（不收集），删除其余节点（收集分数）。
# 目标是最大化收集的分数和 = 总和 - 最小保留和。使用树形DP：
# dp0[u] = 节点u被收集时，其子树满足健康条件的最小保留和（此时每个子节点子树必须健康）
# dp1[u] = 节点u被保留时，其子树的最小保留和 = values[u]（子节点全部可收集）
# 答案为 total - min(dp0[root], dp1[root])。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 将"最大化收集"转化为"最小化保留"
# - 节点保留时，子树可全部收集（该节点保证了路径健康）
# - 节点不保留时，每个子节点子树需独立满足健康条件
