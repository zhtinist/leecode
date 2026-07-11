"""
LeetCode #1443 - Minimum Time to Collect All Apples in a Tree
中文题名：收集树上所有苹果的最少时间
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

Given an undirected tree consisting of `n` vertices numbered from 0 to
`n-1`, which has some apples in their vertices. You spend 1 second to
walk over one edge of the tree. Return the minimum time in seconds you
have to spend in order to collect all apples in the tree starting at vertex
0 and coming back to this vertex.

The edges of the undirected tree are given in the array `edges`, where
`edges[i] = [fromi, toi]` means that exists an edge
connecting the vertices `fromi` and
`toi`. Additionally, there is a boolean array `hasApple`,
where `hasApple[i] = true` means that vertex `i` has
an apple, otherwise, it does not have any apple.

Example 1:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 2:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0

Constraints:

`1 <= n <= 10^5`

`edges.length == n-1`

`edges[i].length == 2`

`0 <= fromi, toi <= n-1`

`fromi < toi`

`hasApple.length == n`

【中文翻译】
给定一棵由 `n` 个顶点组成的无向树，顶点编号从 0 到 `n-1`，树的某些顶点上有苹果。
你走过树的一条边需要 1 秒。返回从顶点 0 出发并返回该顶点，收集树中所有苹果所需的最少时间（秒）。

无向树的边由数组 `edges` 给出，其中 `edges[i] = [fromi, toi]` 表示顶点 `fromi` 和
`toi` 之间存在一条边。此外，还有一个布尔数组 `hasApple`，其中 `hasApple[i] = true`
表示顶点 `i` 有一个苹果，否则表示没有苹果。

示例 1：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
输出：8
解释：上图表示了给定的树，其中红色顶点有苹果。一条收集所有苹果的最优路径由绿色箭头表示。

示例 2：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
输出：6
解释：上图表示了给定的树，其中红色顶点有苹果。一条收集所有苹果的最优路径由绿色箭头表示。

示例 3：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
输出：0

约束条件：

`1 <= n <= 10^5`

`edges.length == n-1`

`edges[i].length == 2`

`0 <= fromi, toi <= n-1`

`fromi < toi`

`hasApple.length == n`
"""

from typing import List, Optional


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int) -> int:
            total_time = 0
            for child in graph[node]:
                if child == parent:
                    continue
                child_time = dfs(child, node)
                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2
            return total_time

        return dfs(0, -1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 从 edges 构建无向邻接表。从节点 0 开始 DFS（传入父节点避免回访）：
# 对于当前节点的每个子节点，递归计算该子树所需时间。
# 如果子节点返回的时间 > 0（子树中有苹果）或子节点本身有苹果，
# 则需要走来回（父到子 + 子到父），累加 child_time + 2。
# 最终返回从 0 出发的总时间。
#
# 时间复杂度: O(N)  -- 每个节点和每条边访问一次
# 空间复杂度: O(N)  -- 邻接表存储 N 个节点和 N-1 条边（每条边存储两次）
#
# 关键点:
# - 无向树需要 parent 参数避免回访，不需要 visited 数组
# - 只有当子树中确实有苹果时才会走过去（+2 表示来回）
# - 叶子节点如果没有苹果返回 0，不会浪费路径









