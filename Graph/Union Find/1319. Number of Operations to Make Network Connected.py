"""
LeetCode #1319 - Number of Operations to Make Network Connected
中文题名：连通网络的操作次数
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

There are `n` computers numbered from `0` to `n-1` connected
by ethernet cables `connections` forming a network where `connections[i]
= [a, b]` represents a connection between computers `a` and `b`.
Any computer can reach any other computer directly or indirectly through the
network.

Given an initial computer network `connections`. You can extract certain
cables between two directly connected computers, and place them between any pair of
disconnected computers to make them directly connected. Return the minimum
number of times you need to do this in order to make all the computers
connected. If it's not possible, return -1.

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0

Constraints:

`1 <= n <= 10^5`

`1 <= connections.length <= min(n*(n-1)/2, 10^5)`

`connections[i].length == 2`

`0 <= connections[i][0], connections[i][1] < n`

`connections[i][0] != connections[i][1]`

There are no repeated connections.

No two computers are connected by more than one cable.

【中文翻译】
有 n 台计算机，编号从 0 到 n-1，通过以太网电缆 connections 连接成网络，
其中 connections[i] = [a, b] 表示计算机 a 和 b 之间的连接。
任何计算机都可以通过网络直接或间接地访问其他计算机。

给定初始计算机网络 connections。你可以拔掉两台直接相连计算机之间的某根电缆，
并将其连接到任意一对未直接相连的计算机之间使其直接连接。
返回使所有计算机连通所需的最少操作次数。如果不可能，返回 -1。

示例 1：
输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔掉计算机 1 和 2 之间的电缆，并将其连接到计算机 1 和 3 之间。

示例 2：
输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
输出：2

示例 3：
输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
输出：-1
解释：电缆数量不足。

示例 4：
输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
输出：0

约束条件：
1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
没有重复的连接。
没有两台计算机通过多于一根电缆连接。
"""

from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already in same component (redundant cable)
        # Union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1
        return True


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Not enough cables to connect all computers
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)
        redundant = 0  # number of redundant cables

        for a, b in connections:
            if not uf.union(a, b):
                redundant += 1

        # Needed operations = number of components - 1
        # (connecting k components requires k-1 cables)
        needed = uf.components - 1

        # Check if we have enough redundant cables
        if redundant >= needed:
            return needed
        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用并查集（Union-Find / Disjoint Set Union）解决连通分量问题。
# 核心思路：
# 1. 最少需要 n-1 根电缆才能连通 n 台计算机（形成一棵树）。
#    如果 connections 的数量小于 n-1，直接返回 -1。
# 2. 遍历所有连接，使用并查集合并相连的计算机。
#    如果一条连接的两个端点已经在同一连通分量中，说明这条电缆是冗余的。
# 3. 处理完后，并查集中的 components 属性表示连通分量的数量。
#    要将 k 个连通分量连接起来，需要 k-1 根电缆。
# 4. 如果冗余电缆数量 >= 需要的电缆数，返回需要的数量；否则返回 -1。
#
# 时间复杂度: O(N + E * α(N))，N 为计算机数，E 为电缆数。
#  α(N) 是反阿克曼函数，近似常数。
# 空间复杂度: O(N)，并查集的 parent 和 rank 数组。
#
# 关键点:
# - 使用并查集统计连通分量数量和冗余边
# - 首先判断 n-1 是否小于等于 cables 总数（必要条件）
# - 每一次合并失败（两端点已在同一分量）即为一条冗余电缆
# - 连通 k 个分量至少需要 k-1 条边
# - 带路径压缩和按秩合并的并查集使 find/union 接近 O(1)
# - 实际上只要 initial check (len(connections) < n-1) 通过，结果总是 components-1










