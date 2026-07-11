"""
LeetCode #2368 - Reachable Nodes With Restrictions
受限条件下可到达节点的数目
https://leetcode.cn/problems/reachable-nodes-with-restrictions/

现有一棵由 `n` 个节点组成的无向树，节点编号从 `0` 到 `n - 1` ，共有 `n - 1` 条边。
给你一个二维整数数组 `edges` ，长度为 `n - 1` ，其中 `edges[i] = [a_i, b_i]` 表示树中节点 `a_i` 和 `b_i` 之间存在一条边。另给你一个整数数组 `restricted` 表示 受限 节点。
在不访问受限节点的前提下，返回你可以从节点 `0` 到达的 最多 节点数目。
注意，节点 `0` 不 会标记为受限节点。

示例 1：
输入：n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5] 输出：4 解释：上图所示正是这棵树。 在不访问受限节点的前提下，只有节点 [0,1,2,3] 可以从节点 0 到达。
示例 2：
输入：n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1] 输出：3 解释：上图所示正是这棵树。 在不访问受限节点的前提下，只有节点 [0,5,6] 可以从节点 0 到达。

提示：
`2 <= n <= 10^5`
`edges.length == n - 1`
`edges[i].length == 2`
`0 <= a_i, b_i < n`
`a_i != b_i`
`edges` 表示一棵有效的树
`1 <= restricted.length < n`
`1 <= restricted[i] < n`
`restricted` 中的所有值 互不相同
"""

from typing import List, Optional


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import deque

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        restricted_set = set(restricted)
        visited = set()
        queue = deque([0])
        visited.add(0)
        count = 0

        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in restricted_set:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Breadth-First Search, Union Find, Graph, Array, Hash Table
#
# 解题思路:
# 首先根据 edges 构建无向图的邻接表。
# 将 restricted 数组转为集合以便 O(1) 查找。
# 从节点 0 开始进行 BFS（或 DFS），跳过受限节点，统计访问到的节点数量。
# 因为题目保证节点 0 不受限，且是一棵树，BFS/DFS 能遍历所有可达节点。
#
# 时间复杂度: O(n) 其中 n 为节点数，每条边和每个节点最多访问一次
# 空间复杂度: O(n) 邻接表和访问集合的开销
#
# 关键点:
# - 使用 set 存储受限节点以实现 O(1) 查找
# - 从节点 0 开始 BFS，保证只访问从 0 可达的节点
# - 树结构确保无环，不会重复访问
