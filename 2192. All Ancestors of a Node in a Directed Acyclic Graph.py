"""
LeetCode #2192 - All Ancestors of a Node in a Directed Acyclic Graph
有向无环图中一个节点的所有祖先
https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

给你一个正整数 `n` ，它表示一个 有向无环图 中节点的数目，节点编号为 `0` 到 `n - 1` （包括两者）。
给你一个二维整数数组 `edges` ，其中 `edges[i] = [from_i, to_i]` 表示图中一条从 `from_i` 到 `to_i` 的单向边。
请你返回一个数组 `answer`，其中 `answer[i]`是第 `i` 个节点的所有 祖先 ，这些祖先节点 升序 排序。
如果 `u` 通过一系列边，能够到达 `v` ，那么我们称节点 `u` 是节点 `v` 的 祖先 节点。

示例 1：

输入：n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]] 输出：[[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]] 解释： 上图为输入所对应的图。 - 节点 0 ，1 和 2 没有任何祖先。 - 节点 3 有 2 个祖先 0 和 1 。 - 节点 4 有 2 个祖先 0 和 2 。 - 节点 5 有 3 个祖先 0 ，1 和 3 。 - 节点 6 有 5 个祖先 0 ，1 ，2 ，3 和 4 。 - 节点 7 有 4 个祖先 0 ，1 ，2 和 3 。
示例 2：

输入：n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] 输出：[[],[0],[0,1],[0,1,2],[0,1,2,3]] 解释： 上图为输入所对应的图。 - 节点 0 没有任何祖先。 - 节点 1 有 1 个祖先 0 。 - 节点 2 有 2 个祖先 0 和 1 。 - 节点 3 有 3 个祖先 0 ，1 和 2 。 - 节点 4 有 4 个祖先 0 ，1 ，2 和 3 。

提示：
`1 <= n <= 1000`
`0 <= edges.length <= min(2000, n * (n - 1) / 2)`
`edges[i].length == 2`
`0 <= from_i, to_i <= n - 1`
`from_i != to_i`
图中不会有重边。
图是 有向 且 无环 的。
"""

from typing import List, Optional


from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        拓扑排序 + DP: 先对有向无环图进行拓扑排序，得到节点的线性顺序。
        然后按拓扑序依次处理每条边 u -> v，将 u 以及 u 的所有祖先加入到 v 的祖先集合中。
        最后对每个节点的祖先集合排序后返回。
        """
        # 构建邻接表和入度数组
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # 拓扑排序
        q = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # 按拓扑序进行 DP：ancestors[v] = ancestors[u] ∪ {u} 对所有边 u -> v
        ancestors = [set() for _ in range(n)]
        for u in topo_order:
            for v in graph[u]:
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])

        # 转为排序列表
        return [sorted(list(a)) for a in ancestors]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Graph, Topological Sort
#
# 解题思路:
# 1. 图是有向无环图(DAG)，可以使用拓扑排序得到节点的线性顺序。
# 2. 构建邻接表 graph[u] = [v1, v2, ...] 表示从 u 到 v 的边。
# 3. 使用 BFS（Kahn 算法）进行拓扑排序，得到 topo_order 列表。
# 4. 按拓扑序进行 DP 转移：对于每条边 u -> v：
#    - 节点 v 的祖先集合 = 节点 v 的原祖先集合 ∪ {u} ∪ 节点 u 的祖先集合。
#    因为按拓扑序处理，当处理到 u 时，u 的祖先已经全部确定。
# 5. 最后将每个节点的祖先集合转为升序列表返回。
#
# 时间复杂度: O(n^2 + m)
# - n <= 1000，拓扑排序 O(n + m)。
# - 最坏情况下（完全 DAG），每个节点的祖先集合大小可达 O(n)，
#   集合合并操作总复杂度 O(n^2)。
# - m <= 2000（边数）。
#
# 空间复杂度: O(n^2)
# - 每个节点的祖先集合最坏大小为 O(n)，总计 O(n^2)。
#
# 关键点:
# - DAG 必定存在拓扑排序，这是 DP 正确性的保证。
# - 按拓扑序处理确保处理 u 时其所有祖先已就绪。
# - 使用 Python set 去重并高效合并（update）。
