"""
LeetCode #785 - Is Graph Bipartite?
中文题名：判断二分图
https://leetcode.com/problems/is-graph-bipartite/

Given an undirected `graph`, return `true` if and only if it is
bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets A and B such that every edge in the graph has one node in A and
another node in B.

The graph is given in the following form: `graph[i]` is a list of indexes
`j` for which the edge between nodes `i` and `j` exists.
Each node is an integer between `0` and `graph.length - 1`.
There are no self edges or parallel edges: `graph[i]` does not contain
`i`, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

Note:

`graph` will have length in range `[1, 100]`.

`graph[i]` will contain integers in range `[0, graph.length - 1]`.

`graph[i]` will not contain `i` or duplicate values.

The graph is undirected: if any element `j` is in `graph[i]`, then
`i` will be in `graph[j]`.

【中文翻译】
给定一个无向图 `graph`，当且仅当它是二分图时返回 `true`。

回顾一下，如果一个图是二分图，那么我们可以将它的节点集合划分为两个独立的子集 A 和 B，使得图中的每条边的一个节点在 A 中，另一个节点在 B 中。

图以下列形式给出：`graph[i]` 是索引 `j` 的列表，表示节点 `i` 和 `j` 之间存在边。每个节点是 `0` 到 `graph.length - 1` 之间的整数。没有自环或平行边：`graph[i]` 不包含 `i`，也不包含任何重复元素。

示例 1：
输入：[[1,3], [0,2], [1,3], [0,2]]
输出：true
解释：可以将顶点分成两组：{0, 2} 和 {1, 3}。

示例 2：
输入：[[1,2,3], [0,2], [0,1,3], [0,2]]
输出：false
解释：无法将节点集合分成两个独立子集。

注意：

`graph` 的长度范围在 `[1, 100]`。

`graph[i]` 包含范围在 `[0, graph.length - 1]` 内的整数。

`graph[i]` 不包含 `i` 或重复值。

图是无向的：如果 `j` 在 `graph[i]` 中，那么 `i` 也在 `graph[j]` 中。
"""

from typing import List, Optional


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1: uncolored, 0: group A, 1: group B

        for i in range(n):
            if color[i] == -1:
                # BFS
                from collections import deque
                q = deque([i])
                color[i] = 0
                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]
                            q.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 图染色（BFS/DFS）。
# 二分图等价于可以用两种颜色给所有节点染色，使得每条边的两个端点颜色不同。
# 1. 使用数组 color 标记每个节点的颜色：-1 表示未染色，0 和 1 表示两种颜色。
# 2. 遍历所有节点，对每个未染色的节点进行 BFS（或 DFS）。
# 3. BFS 过程中：
#    - 当前节点的邻居未染色时，染成相反颜色（1 - color[node]）。
#    - 如果邻居已染色且与当前节点同色，说明冲突，返回 False。
# 4. 图可能不连通，需要检查所有连通分量。
# 5. 所有连通分量都满足条件时返回 True。
#
# 时间复杂度: O(V + E) - 每个节点和边访问一次
# 空间复杂度: O(V) - color 数组和队列
#
# 关键点:
# - 二分图 <=> 可二染色
# - BFS/DFS 遍历，给邻居染相反色
# - 同色冲突即非二分图
# - 图可能不连通，需遍历所有节点
