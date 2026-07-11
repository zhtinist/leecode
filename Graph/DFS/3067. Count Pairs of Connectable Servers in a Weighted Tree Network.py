"""
LeetCode #3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
在带权树网络中统计可连接服务器对数目
https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

给你一棵无根带权树，树中总共有 `n` 个节点，分别表示 `n` 个服务器，服务器从 `0` 到 `n - 1` 编号。同时给你一个数组 `edges` ，其中 `edges[i] = [a_i, b_i, weight_i]` 表示节点 `a_i` 和 `b_i` 之间有一条双向边，边的权值为 `weight_i` 。再给你一个整数 `signalSpeed` 。
如果两台服务器 `a` 和 `b` 是通过服务器 `c` 可连接的，则：
`a < b` ，`a != c` 且 `b != c` 。
从 `c` 到 `a` 的距离是可以被 `signalSpeed` 整除的。
从 `c` 到 `b` 的距离是可以被 `signalSpeed` 整除的。
从 `c` 到 `b` 的路径与从 `c` 到 `a` 的路径没有任何公共边。
请你返回一个长度为 `n` 的整数数组 `count` ，其中 `count[i]` 表示通过服务器 `i` 可连接 的服务器对的 数目 。

示例 1：

输入：edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1 输出：[0,4,6,6,4,0] 解释：由于 signalSpeed 等于 1 ，count[c] 等于所有从 c 开始且没有公共边的路径对数目。 在输入图中，count[c] 等于服务器 c 左边服务器数目乘以右边服务器数目。
示例 2：

输入：edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3 输出：[2,0,0,0,0,0,2] 解释：通过服务器 0 ，有 2 个可连接服务器对(4, 5) 和 (4, 6) 。 通过服务器 6 ，有 2 个可连接服务器对 (4, 5) 和 (0, 5) 。 所有服务器对都必须通过服务器 0 或 6 才可连接，所以其他服务器对应的可连接服务器对数目都为 0 。

提示：
`2 <= n <= 1000`
`edges.length == n - 1`
`edges[i].length == 3`
`0 <= a_i, b_i < n`
`edges[i] = [a_i, b_i, weight_i]`
`1 <= weight_i <= 10^6`
`1 <= signalSpeed <= 10^6`
输入保证 `edges` 构成一棵合法的树。
"""

from typing import List, Optional


class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:
        """
        For each node c, treat it as center. For each neighbor,
        DFS to count nodes in that subtree where distance from c
        is divisible by signalSpeed. Pairs = sum of products of
        counts from different subtrees.
        """
        n = len(edges) + 1
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        ans = [0] * n

        for c in range(n):
            subtree_counts = []

            for nxt, w in adj[c]:
                # DFS into this subtree, counting nodes divisible by signalSpeed
                def dfs(node: int, parent: int, dist: int) -> int:
                    cnt = 1 if dist % signalSpeed == 0 else 0
                    for nb, weight in adj[node]:
                        if nb != parent:
                            cnt += dfs(nb, node, dist + weight)
                    return cnt

                cnt = dfs(nxt, c, w)
                subtree_counts.append(cnt)

            # Count pairs from different subtrees
            total = 0
            for i in range(len(subtree_counts)):
                for j in range(i + 1, len(subtree_counts)):
                    total += subtree_counts[i] * subtree_counts[j]
            ans[c] = total

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Array
#
# 解题思路:
# 对每个节点 c 作为中心，枚举其每个邻居出发的子树，DFS 统计该子树中到 c 的距离能被 signalSpeed 整除的节点数。
# a 和 b 必须来自不同子树（保证路径无公共边），且距离都能被 signalSpeed 整除。
# 对于 c 的各子树计数 cnt1, cnt2, ..., cntk，可连接服务器对数为 sum(cnt_i * cnt_j)，其中 i < j。
#
# 时间复杂度: O(n^2)，每个节点作为中心执行一次 O(n) DFS
# 空间复杂度: O(n)，邻接表和递归栈
#
# 关键点:
# - a 和 b 必须来自 c 的不同邻居子树，保证路径无公共边
# - 距离整除条件在 DFS 中逐边累加判断
# - 计数对数量 = 不同子树计数两两乘积之和
