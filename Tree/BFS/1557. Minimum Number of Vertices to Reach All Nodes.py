"""
LeetCode #1557 - Minimum Number of Vertices to Reach All Nodes
中文题名：可以到达所有点的最少点数目
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/


Given a directed acyclic graph, with `n` vertices
numbered from `0` to `n-1`, and an array `edges` where `edges[i]
= [fromi, toi]` represents a directed edge from
node `fromi` to node `toi`.

Find the smallest set of vertices from which all nodes in the graph are
reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

Example 2:

Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.

Constraints:

`2 <= n <= 10^5`

`1 <= edges.length <= min(10^5, n * (n - 1) / 2)`

`edges[i].length == 2`

`0 <= fromi, toi < n`

All pairs `(fromi, toi)` are distinct.

【中文翻译】
给定一个有向无环图，包含 n 个节点（编号 0 到 n-1）和一个边列表 edges，
其中 edges[i] = [from_i, to_i] 表示一条从 from_i 到 to_i 的有向边。
找出最小的节点集合，使得从集合中的节点出发可以到达图中的所有节点。

示例 1：
输入：n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
输出：[0,3]

示例 2：
输入：n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
输出：[0,2,3]
"""

from typing import List, Optional


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
        return [i for i in range(n) if indegree[i] == 0]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于图是有向无环图（DAG），任何入度为 0 的节点必须被包含在答案中，
# 因为没有其他节点可以到达它们。而所有入度 > 0 的节点都可以从某个入度为 0 的节点到达。
# 因此，答案就是所有入度为 0 的节点集合。
#
# 时间复杂度: O(N + E) — 计算入度
# 空间复杂度: O(N) — 入度数组
#
# 关键点:
# - DAG 中入度为 0 的节点是最小可达集合
# - 无需 BFS/DFS，只需计算入度
# - 所有入度 > 0 的节点都可以从入度为 0 的节点出发到达












