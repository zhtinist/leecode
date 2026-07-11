"""
LeetCode #1129 - Shortest Path with Alternating Colors
中文题名：颜色交替的最短路径
https://leetcode.com/problems/shortest-path-with-alternating-colors/

Consider a directed graph, with nodes labelled `0, 1, ..., n-1`.  In this
graph, each edge is either red or blue, and there could be self-edges or parallel
edges.

Each `[i, j]` in `red_edges` denotes a red directed edge from node
`i` to node `j`.  Similarly, each `[i, j]` in `blue_edges`
denotes a blue directed edge from node `i` to node `j`.

Return an array `answer` of length `n`, where
each `answer[X]` is the length of the shortest path from node
`0` to node `X` such that the edge colors alternate along
the path (or `-1` if such a path doesn't exist).

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]

Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]

Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]

Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]

Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]

Constraints:

`1 <= n <= 100`

`red_edges.length <= 400`

`blue_edges.length <= 400`

`red_edges[i].length == blue_edges[i].length == 2`

`0 <= red_edges[i][j], blue_edges[i][j] < n`

【中文翻译】
考虑一个有向图，节点标记为 0, 1, ..., n-1。在这个图中，每条边要么是红色要么是蓝色，且可能存在自环或平行边。

red_edges 中的每个 [i, j] 表示从节点 i 到节点 j 的一条红色有向边。
类似地，blue_edges 中的每个 [i, j] 表示从节点 i 到节点 j 的一条蓝色有向边。

返回一个长度为 n 的数组 answer，其中每个 answer[X] 是从节点 0 到节点 X 的最短路径的长度，
该路径要求边的颜色交替变化（如果不存在这样的路径则为 -1）。

示例 1：

输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]

示例 2：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]

示例 3：

输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]

示例 4：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]

示例 5：

输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]

约束条件：

`1 <= n <= 100`

`red_edges.length <= 400`

`blue_edges.length <= 400`

`red_edges[i].length == blue_edges[i].length == 2`

`0 <= red_edges[i][j], blue_edges[i][j] < n`
"""

from typing import List, Optional


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1
        graph = [[[], []] for _ in range(n)]
        for u, v in red_edges:
            graph[u][RED].append(v)
        for u, v in blue_edges:
            graph[u][BLUE].append(v)

        from collections import deque
        dist = [[-1, -1] for _ in range(n)]
        dist[0][RED] = dist[0][BLUE] = 0
        q = deque([(0, RED), (0, BLUE)])

        while q:
            node, color = q.popleft()
            next_color = 1 - color
            for neighbor in graph[node][next_color]:
                if dist[neighbor][next_color] == -1:
                    dist[neighbor][next_color] = dist[node][color] + 1
                    q.append((neighbor, next_color))

        ans = []
        for d in dist:
            r, b = d[RED], d[BLUE]
            if r == -1 and b == -1:
                ans.append(-1)
            elif r == -1:
                ans.append(b)
            elif b == -1:
                ans.append(r)
            else:
                ans.append(min(r, b))
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS 在状态空间 (node, last_edge_color) 上搜索最短路径。
# 1. 构建邻接表：为每个节点维护两个列表，分别存储红色出边和蓝色出边。
# 2. 用二维数组 dist[node][color] 记录到达节点 node 且最后一条边为 color 的最短距离。
#    初始 dist[0][RED] = dist[0][BLUE] = 0（从节点 0 出发，可以选红或蓝作为"上一次"的颜色）。
# 3. BFS 队列初始包含 (0, RED) 和 (0, BLUE)。
# 4. 每次出队 (node, color)，遍历 graph[node][1-color]（颜色必须交替），
#    若 neighbor 在该颜色下未被访问，更新距离并入队。
# 5. 最终每个节点的答案为 min(dist[node][RED], dist[node][BLUE])（若两者都是 -1 则答案为 -1）。
#
# 时间复杂度: O(n + m) - 每条边最多被访问两次（从不同颜色状态进入）
# 空间复杂度: O(n + m) - 邻接表和距离数组
#
# 关键点:
# - 状态定义为 (节点, 上一条边的颜色)，因为到达同一节点的不同颜色状态会导致不同的后续路径
# - 初始时将两种颜色都入队（视为从节点 0 出发时没有"上一次"的颜色限制）
# - BFS 天然保证首次访问时距离最短
