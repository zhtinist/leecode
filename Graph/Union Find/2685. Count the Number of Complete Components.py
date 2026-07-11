"""
LeetCode #2685 - Count the Number of Complete Components
统计完全连通分量的数量
https://leetcode.cn/problems/count-the-number-of-complete-components/

给你一个整数 `n` 。现有一个包含 `n` 个顶点的 无向 图，顶点按从 `0` 到 `n - 1` 编号。给你一个二维整数数组 `edges` 其中 `edges[i] = [a_i, b_i]` 表示顶点 `a_i` 和 `b_i` 之间存在一条 无向 边。
返回图中 完全连通分量 的数量。
如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。
如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。

示例 1：

输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]] 输出：3 解释：如上图所示，可以看到此图所有分量都是完全连通分量。
示例 2：

输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]] 输出：1 解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。 包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。 因此，在图中完全连接分量的数量是 1 。

提示：
`1 <= n <= 50`
`0 <= edges.length <= n * (n - 1) / 2`
`edges[i].length == 2`
`0 <= a_i, b_i <= n - 1`
`a_i != b_i`
不存在重复的边
"""

from typing import List, Optional


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque

        # build adjacency list
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i]:
                continue
            # BFS to find connected component
            q = deque([i])
            visited[i] = True
            comp = []
            while q:
                u = q.popleft()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)

            # check if component is complete
            k = len(comp)
            # in a complete component, each node has degree k-1
            is_complete = all(len(adj[u]) == k - 1 for u in comp)
            if is_complete:
                ans += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Union Find, Graph
#
# 解题思路:
# 使用BFS/DFS找出图中的所有连通分量。对每个分量，检查是否是完全连通分量：
# 对于k个节点的完全图，每个节点的度数应为k-1（分量内每对节点都有边）。
# 由于连通分量定义保证没有边通向外部，只需检查每个节点度数是否等于k-1。
#
# 时间复杂度: O(n + e)
# 空间复杂度: O(n + e)
#
# 关键点:
# - 连通分量 = BFS/DFS找到的所有连通子图
# - 完全连通 = 每对节点之间都有边
# - k个节点的完全图中每个节点度数=k-1
