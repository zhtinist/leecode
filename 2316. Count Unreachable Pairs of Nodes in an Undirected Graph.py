"""
LeetCode #2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
统计无向图中无法互相到达点对数
https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

给你一个整数 `n` ，表示一张 无向图 中有 `n` 个节点，编号为 `0` 到 `n - 1` 。同时给你一个二维整数数组 `edges` ，其中 `edges[i] = [a_i, b_i]` 表示节点 `a_i` 和 `b_i` 之间有一条 无向 边。
请你返回 无法互相到达 的不同 点对数目 。

示例 1：

输入：n = 3, edges = [[0,1],[0,2],[1,2]] 输出：0 解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。
示例 2：

输入：n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]] 输出：14 解释：总共有 14 个点对互相无法到达： [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]] 所以我们返回 14 。

提示：
`1 <= n <= 10^5`
`0 <= edges.length <= 2 * 10^5`
`edges[i].length == 2`
`0 <= a_i, b_i < n`
`a_i != b_i`
不会有重复边。
"""

from typing import List, Optional


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            # 路径压缩
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px == py:
                return
            # 按大小合并：将较小的集合合并到较大的集合
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]

        # 构建并查集
        for u, v in edges:
            union(u, v)

        # 统计不可达点对
        # 对于每个连通分量，它与之前处理过的所有节点都无法互相到达
        answer = 0
        total_seen = 0
        for i in range(n):
            if find(i) == i:  # 是连通分量的根节点
                comp_size = size[i]
                # 当前分量中的每个节点，与之前所有分量中的节点都不可达
                answer += comp_size * total_seen
                total_seen += comp_size

        return answer


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Union Find, Graph
#
# 解题思路:
# 使用并查集（Union-Find / DSU）将图划分为连通分量。两个节点无法互相到达，
# 当且仅当它们属于不同的连通分量。
#
# 设各连通分量大小分别为 s1, s2, ..., sk。所有点对总数为 n×(n-1)/2。
# 不可达点对 = 总点对数 - 各分量内部可达点对数
#          = n×(n-1)/2 - Σ(si×(si-1)/2)
#
# 也可以直接累计：遍历每个分量，对于大小为 s 的分量，它与之前已处理的所有节点
# （总数记为 total_seen）之间的所有 s × total_seen 个点对都不可达。这种方法
# 避免了计算总点对数的溢出问题。
#
# 时间复杂度: O(n + e × α(n))，其中 α(n) 是反阿克曼函数，近似常数。
#            实际接近 O(n + e)。
# 空间复杂度: O(n)，用于存储 parent 和 size 数组。
#
# 关键点:
# - 使用并查集高效合并连通分量，带路径压缩和按大小合并优化。
# - 利用"增量统计"方法：每遇到一个新分量 s，它与之前所有节点组成的点对均不可达。
# - 最后返回的答案无需取模（结果在 64 位整数范围内）。
