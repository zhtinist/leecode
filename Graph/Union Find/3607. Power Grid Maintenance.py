"""
LeetCode #3607 - Power Grid Maintenance
电网维护
https://leetcode.cn/problems/power-grid-maintenance/

给你一个整数 `c`，表示 `c` 个电站，每个电站有一个唯一标识符 `id`，从 1 到 `c` 编号。
这些电站通过 `n` 条 双向 电缆互相连接，表示为一个二维数组 `connections`，其中每个元素 `connections[i] = [u_i, v_i]` 表示电站 `u_i` 和电站 `v_i` 之间的连接。直接或间接连接的电站组成了一个 电网 。
最初，所有 电站均处于在线（正常运行）状态。
另给你一个二维数组 `queries`，其中每个查询属于以下 两种类型之一 ：

`[1, x]`：请求对电站 `x` 进行维护检查。如果电站 `x` 在线，则它自行解决检查。如果电站 `x` 已离线，则检查由与 `x` 同一 电网 中 编号最小 的在线电站解决。如果该电网中 不存在 任何 在线 电站，则返回 -1。

`[2, x]`：电站 `x` 离线（即变为非运行状态）。
返回一个整数数组，表示按照查询中出现的顺序，所有类型为 `[1, x]` 的查询结果。
注意：电网的结构是固定的；离线（非运行）的节点仍然属于其所在的电网，且离线操作不会改变电网的连接性。

示例 1：

输入： c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
输出： [3,2,3]
解释：

最初，所有电站 `{1, 2, 3, 4, 5}` 都在线，并组成一个电网。
查询 `[1,3]`：电站 3 在线，因此维护检查由电站 3 自行解决。
查询 `[2,1]`：电站 1 离线。剩余在线电站为 `{2, 3, 4, 5}`。
查询 `[1,1]`：电站 1 离线，因此检查由电网中编号最小的在线电站解决，即电站 2。
查询 `[2,2]`：电站 2 离线。剩余在线电站为 `{3, 4, 5}`。
查询 `[1,2]`：电站 2 离线，因此检查由电网中编号最小的在线电站解决，即电站 3。
示例 2：

输入： c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]
输出： [1,-1]
解释：
没有连接，因此每个电站是一个独立的电网。
查询 `[1,1]`：电站 1 在线，且属于其独立电网，因此维护检查由电站 1 自行解决。
查询 `[2,1]`：电站 1 离线。
查询 `[1,1]`：电站 1 离线，且其电网中没有其他电站，因此结果为 -1。

提示：
`1 <= c <= 10^5`
`0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)`
`connections[i].length == 2`
`1 <= u_i, v_i <= c`
`u_i != v_i`
`1 <= queries.length <= 2 * 10^5`
`queries[i].length == 2`
`queries[i][0]` 为 1 或 2。
`1 <= queries[i][1] <= c`
"""

from typing import List, Optional


class Solution:
    def powerGridMaintenance(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Build adjacency list (1-indexed)
        adj = [[] for _ in range(c + 1)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Determine which stations are taken offline in forward processing
        offline_set = set()
        for typ, x in queries:
            if typ == 2:
                offline_set.add(x)

        # In reverse processing: stations NEVER taken offline are initially online
        online = [False] * (c + 1)
        for i in range(1, c + 1):
            if i not in offline_set:
                online[i] = True

        # DSU (Union-Find) arrays
        parent = list(range(c + 1))
        # min_online[i]: minimum online node id in the component of node i
        min_online = [i if online[i] else float('inf') for i in range(c + 1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            parent[rx] = ry
            min_online[ry] = min(min_online[ry], min_online[rx])

        # Union initially online stations that are directly connected
        for u, v in connections:
            if online[u] and online[v]:
                union(u, v)

        # Process queries in reverse
        ans = []
        for typ, x in reversed(queries):
            if typ == 1:
                root = find(x)
                val = min_online[root]
                ans.append(val if val != float('inf') else -1)
            else:  # typ == 2: bring station x back online
                online[x] = True
                root = find(x)
                min_online[root] = min(min_online[root], x)
                for nb in adj[x]:
                    if online[nb]:
                        union(x, nb)

        ans.reverse()
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Union Find, Graph, Array, Hash Table, Ordered Set, Heap (Priority Queue)
#
# 解题思路:
# 核心技巧：离线逆序处理（offline reverse processing）。
# 在正向处理中，查询类型 2 将电站下线，而并查集（DSU）不支持删除操作。
# 但在逆序处理中，类型 2 变为"将电站恢复上线"，DSU 可以支持添加（union）。
# 具体流程：
# 1. 预先扫描所有查询，记录被下线过的电站集合
# 2. 初始状态（逆序起点）：从未被下线的电站设为在线
# 3. 用 DSU 维护每个电网（连通分量）中编号最小的在线电站
# 4. 逆序遍历查询：类型 1 直接查询当前 DSU 中该电站所在分量的最小在线电站
#    类型 2 将该电站恢复在线，并与相邻的在线电站 union
# 5. 将收集的答案逆序后返回
#
# 时间复杂度: O((c + connections.length + queries.length) * α(c)) — 近似线性，α 为反阿克曼函数
# 空间复杂度: O(c + connections.length + queries.length) — 邻接表、DSU 数组、答案数组
#
# 关键点:
# - 逆序处理将"删除"变为"添加"，使 DSU 可用
# - 每个 DSU 集合维护最小在线节点编号 min_online
# - 恢复上线时需更新 min_online 并 union 相邻在线节点
# - 注意处理没有任何在线电站的情况，返回 -1
