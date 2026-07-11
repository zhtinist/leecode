"""
LeetCode #797 - All Paths From Source to Target
中文题名：所有可能的路径
https://leetcode.com/problems/all-paths-from-source-to-target/

Given a directed, acyclic graph of `N` nodes.  Find all possible paths from
node `0` to node `N-1`, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

The number of nodes in the graph will be in the range `[2, 15]`.

You can print different paths in any order, but you should keep the order of nodes
inside one path.

【中文翻译】
给定一个有 `N` 个节点的有向无环图，找出所有从节点 `0` 到节点 `N-1` 的路径，并以任意顺序返回。

图的表示方法如下：节点为 0, 1, ..., graph.length - 1。
graph[i] 是包含所有边 (i, j) 中的节点 j 的列表。

示例：
输入：[[1,2], [3], [3], []]
输出：[[0,1,3],[0,2,3]]
解释：图如下所示：
0--->1
|    |
v    v
2--->3
共有两条路径：0 -> 1 -> 3 和 0 -> 2 -> 3。

注意：
图中节点的数量将在 `[2, 15]` 范围内。
你可以以任意顺序返回不同的路径，但应保持一条路径中节点的顺序。
"""

from typing import List, Optional


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result: List[List[int]] = []

        def dfs(node: int, path: List[int]) -> None:
            if node == target:
                result.append(path[:])
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(0, [0])
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用深度优先搜索（DFS）遍历有向无环图（DAG）。
# 从节点 0 出发，维护当前路径。每到达一个节点，
# 将其加入路径；如果到达目标节点 N-1，将当前路径的
# 副本添加到结果中；否则继续向邻居节点递归。
# 回溯时从路径中移除当前节点。
#
# 时间复杂度: O(2^N * N) - 最坏情况有 2^(N-2) 条路径，
#   每条路径长度为 N，复制路径需要 O(N)
# 空间复杂度: O(N) - 递归栈深度和路径存储
#
# 关键点:
# - 题目保证图为有向无环图（DAG），不需要环检测
# - 回溯时使用 path[:] 进行深拷贝
# - N <= 15，2^15 = 32768 可以接受
