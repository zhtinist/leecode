"""
LeetCode #399 - Evaluate Division
中文题名：除法求值
https://leetcode.com/problems/evaluate-division/

Equations are given in the format `A / B = k`, where `A` and
`B` are variables represented as strings, and `k` is a real number
(floating point number). Given some queries, return the answers. If the answer does not
exist, return `-1.0`.

Example:

Given ` a / b = 2.0, b / c = 3.0.`

queries are: ` a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .`

return ` [6.0, 0.5, -1.0, 1.0, -1.0 ].`

The input is: ` vector<pair<string, string>> equations, vector<double>&
values, vector<pair<string, string>> queries `, where `equations.size()
== values.size()`, and the values are positive. This represents the equations. Return
` vector<double>`.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid. You may assume that evaluating the queries will result in no
division by zero and there is no contradiction.

【中文翻译】
方程式以 A / B = k 的格式给出，其中 A 和 B 是用字符串表示的变量，k 是一个实数（浮点数）。给定一些查询，返回答案。如果答案不存在，返回 -1.0。

示例：

给定 a / b = 2.0, b / c = 3.0。

查询为：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?

返回 [6.0, 0.5, -1.0, 1.0, -1.0]。

输入为：vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries，其中 equations.size() == values.size()，且值为正数。这代表了一组方程式。返回 vector<double>。

根据上述示例：

equations = [["a", "b"], ["b", "c"]],
values = [2.0, 3.0],
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]。

输入始终有效。你可以假设计算查询不会导致除以零，且没有矛盾。
"""

from typing import List, Optional
from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            queue = deque([(start, 1.0)])
            visited = {start}
            while queue:
                node, cur_val = queue.popleft()
                for neighbor, weight in graph[node]:
                    if neighbor == end:
                        return cur_val * weight
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, cur_val * weight))
            return -1.0

        return [bfs(a, b) for a, b in queries]











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将问题建模为带权有向图。变量为节点，除法关系为边。
# 若 a/b = k，则添加边 a→b（权重 k）和 b→a（权重 1/k）。
# 对于每个查询 query(a, b)：
# - 如果 a 或 b 不在图中，返回 -1.0
# - 如果 a == b 且都在图中，返回 1.0
# - 否则通过 BFS 从 a 搜索到 b，路径上权重累乘即为结果
# 也可用带权并查集（Union Find）优化，预处理后将单个查询优化到 O(α(N))。
#
# 时间复杂度: O(V + E + Q*(V+E)) - 建图 O(V+E)，每个查询 BFS 最坏 O(V+E)
# 空间复杂度: O(V + E) - 邻接表存储图
#
# 关键点:
# - 将除法关系建模为有向带权图
# - a/b = k → a→b 权重 k，b→a 权重 1/k
# - BFS/DFS 沿路径累积权重的乘积
# - 更优方案：带权并查集，将查询优化到近 O(1)
# - 注意处理节点不存在和 a==b 的边界情况
