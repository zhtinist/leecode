"""
LeetCode #1466 - Reorder Routes to Make All Paths Lead to the City Zero
中文题名：重新规划路线
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

There are `n` cities numbered from `0` to `n-1`
and `n-1` roads such that there is only one way to travel between
two different cities (this network form a tree). Last year, The ministry
of transport decided to orient the roads in one direction because they are too
narrow.

Roads are represented by `connections` where `connections[i]
= [a, b]` represents a road from city `a` to `b`.

This year, there will be a big event in the capital (city 0), and many people want to
travel to this city.

Your task consists of reorienting some roads such that each city can visit the
city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:

`2 <= n <= 5 * 10^4`

`connections.length == n-1`

`connections[i].length == 2`

`0 <= connections[i][0], connections[i][1] <= n-1`

`connections[i][0] != connections[i][1]`

【中文翻译】
有 `n` 个城市，编号从 `0` 到 `n-1`，以及 `n-1` 条道路，
使得任意两个不同城市之间只有一条路可走（这个网络形成一棵树）。
去年，交通部决定将道路定向为单向，因为道路太窄。

道路由 `connections` 表示，其中 `connections[i] = [a, b]`
表示一条从城市 `a` 到城市 `b` 的道路。

今年，首都（城市 0）将举办一场大型活动，许多人想要前往这座城市。

你的任务是重新定向某些道路，使得每个城市都能到达城市 0。
返回最少需要改变的边数。

保证重新定向后每个城市都可以到达城市 0。

示例 1：

输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：改变图中红色所示边的方向，使每个节点都能到达节点 0（首都）。

示例 2：

输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：改变图中红色所示边的方向，使每个节点都能到达节点 0（首都）。

示例 3：

输入：n = 3, connections = [[1,0],[2,0]]
输出：0

约束条件：

`2 <= n <= 5 * 10^4`

`connections.length == n-1`

`connections[i].length == 2`

`0 <= connections[i][0], connections[i][1] <= n-1`

`connections[i][0] != connections[i][1]`
"""

from typing import List, Optional


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        count = 0
        stack = [0]
        visited = [False] * n
        visited[0] = True

        while stack:
            node = stack.pop()
            for neighbor, direction in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += direction
                    stack.append(neighbor)

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将原始有向图转换为无向图，但为每条边标记方向：
# direction=1 表示原始边从当前节点指向邻居（需要翻转），
# direction=0 表示原始边从邻居指向当前节点（不需要翻转）。
# 从节点 0 开始 DFS/迭代遍历树：
# 对于每条边，如果原始方向是离开 0（direction=1），则需要翻转，count++。
# 最终 count 即为最少需要改变的边数。
#
# 时间复杂度: O(N)  -- 每个节点和每条边访问一次
# 空间复杂度: O(N)  -- 邻接表存储图
#
# 关键点:
# - 从 0 向外 DFS，所有边都需要指向 0（即指向父节点方向）
# - 用 (neighbor, direction) 标记原始方向，direction=1 表示需要翻转
# - 树结构保证无环，visited 数组防止回访即可









