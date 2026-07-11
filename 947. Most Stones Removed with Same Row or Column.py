"""
LeetCode #947 - Most Stones Removed with Same Row or Column
中文题名：移除最多的同行或同列石头
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point
may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with
another stone on the grid.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:

Input: stones = [[0,0]]
Output: 0

Note:

`1 <= stones.length <= 1000`

`0 <= stones[i][j] < 10000`

【中文翻译】
在一个二维平面上，我们将石头放置在一些整数坐标点上。每个坐标点最多只能有一块石头。

现在，一次操作包括移除一块与网格中另一块石头共享同一列或同一行的石头。

我们最多可以进行多少次操作？

"""

from typing import List, Optional


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Offset row index to avoid collision with column indices
        for row, col in stones:
            union(row, ~col)  # use ~col to distinguish row from column

        # Count unique connected components
        components = set()
        for row, col in stones:
            components.add(find(row))

        return len(stones) - len(components)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 问题转化为图论：将每块石头视为图中的节点。如果两块石头共享同一行或同一列，
#    则在它们之间连一条边。问题变为：在每个连通分量中，最多可以移除 n-1 块石头
#    （保留一块作为根基），因此总移除数量 = 总石头数 - 连通分量数。
# 2. 并查集实现：使用 Union-Find 将同行或同列的石头合并到同一个集合。
#    关键技巧 — 用 ~col（按位取反）将列索引转换为负数，与行索引区分开，
#    避免行号与列号冲突。
# 3. 统计连通分量：遍历所有石头，用 find 找出它们所属的根节点，去重后
#    即为连通分量数。
# 4. 返回 len(stones) - 连通分量数。
#
# 时间复杂度: O(N * α(N)) — 近似 O(N)，其中 α 是阿克曼反函数，N 是石头数。
# 空间复杂度: O(N) — 并查集的父节点映射。
#
# 关键点:
# - 核心洞察：每个连通分量可以保留一块石头，其余全部移除
# - 使用 ~col 技巧将行和列编码到不同命名空间（避免行号 0 和列号 0 冲突）
# - 并查集的路径压缩优化
