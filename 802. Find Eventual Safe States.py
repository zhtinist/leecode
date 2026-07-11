"""
LeetCode #802 - Find Eventual Safe States
中文题名：找到最终的安全状态
https://leetcode.com/problems/find-eventual-safe-states/

In a directed graph, we start at some node and every turn, walk along a directed edge of the
graph.  If we reach a node that is terminal (that is, it has no outgoing directed
edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually
walk to a terminal node.  More specifically, there exists a natural number
`K` so that for any choice of where to walk, we must have stopped at a terminal
node in less than `K` steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has `N` nodes with labels `0, 1, ..., N-1`, where
`N` is the length of `graph`.  The graph is given in the
following form: `graph[i]` is a list of labels `j` such that `(i,
j)` is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Note:

`graph` will have length at most `10000`.

The number of edges in the graph will not exceed `32000`.

Each `graph[i]` will be a sorted list of different integers, chosen within
the range `[0, graph.length - 1]`.

【中文翻译】
在一个有向图中，我们从某个节点出发，每一步沿有向边移动。如果我们到达一个终端节点（即没有出边的节点），则停止。

现在我们定义一个起始节点是"最终安全的"，当且仅当无论我们如何选择路径，都必然最终到达一个终端节点。更具体地说，存在一个自然数 `K`，对于任何行走选择，我们必须在少于 `K` 步内停在一个终端节点上。

哪些节点是最终安全的？将它们按排序顺序作为数组返回。

有向图有 `N` 个节点，标签为 `0, 1, ..., N-1`，其中 `N` 是 `graph` 的长度。图的表示形式为：`graph[i]` 是标签 `j` 的列表，表示 `(i, j)` 是图中的一条有向边。

示例：
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]
以下是上述图的示意图。

注意：
`graph` 的长度最大为 `10000`。
图中的边数不超过 `32000`。
每个 `graph[i]` 是不同整数的排序列表，范围在 `[0, graph.length - 1]` 内。
"""

from typing import List, Optional


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # out_degree[i] = number of outgoing edges from node i
        out_degree = [len(graph[i]) for i in range(n)]
        # reverse_graph[j] = list of nodes i where i -> j
        reverse_graph: List[List[int]] = [[] for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                reverse_graph[j].append(i)

        # Start with terminal nodes (out_degree == 0)
        from collections import deque
        queue: deque = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True
            # All predecessors of this safe node have one less "unsafe" edge
            for prev in reverse_graph[node]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    queue.append(prev)

        return [i for i in range(n) if safe[i]]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用拓扑排序（Kahn 算法）的变体，从终点反推安全节点。
# 1. 构建反向图 reverse_graph：存储每条边的反向。
# 2. 计算每个节点的出度 out_degree。
# 3. 将所有出度为 0 的节点（终端节点）加入队列，它们天然安全。
# 4. BFS 处理：每次从队列取出一个安全节点，
#    将其所有前驱节点的出度减 1（相当于移除这条已确认安全的边）。
#    如果前驱节点的出度变为 0，说明它的所有出边都通向安全节点，
#    该前驱节点也是安全的，加入队列。
# 5. 最终所有被标记为安全的节点即为答案。
#
# 时间复杂度: O(V + E) - 每个节点和每条边处理一次
# 空间复杂度: O(V + E) - 反向图存储和队列
#
# 关键点:
# - 从终点（出度为 0）反向拓扑排序，找出所有不会进入环的节点
# - 反向图的构建是关键：需要知道哪些节点指向当前安全节点
# - 可以理解为：把所有边反向，从终端节点 BFS，
#   能到达的节点都是安全的
# - 结果不需要另外排序，按 0 到 N-1 遍历 safe 数组即可
