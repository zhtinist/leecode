"""
LeetCode #959 - Regions Cut By Slashes
中文题名：由斜杠划分区域
https://leetcode.com/problems/regions-cut-by-slashes/

In a N x N `grid` composed of 1 x 1 squares, each 1 x 1 square consists of a
`/`, `\`, or blank space.  These characters divide the square
into contiguous regions.

(Note that backslash characters are escaped, so a `\` is represented as
`"\\"`.)

Return the number of regions.

【中文翻译】
在一个由 1 x 1 方格组成的 N x N 网格 `grid` 中，每个 1 x 1 方格由 `/`、`\`
或空格组成。这些字符将方格划分为若干连续区域。
（注意，反斜杠字符是转义的，因此 `\` 用 `"\\"` 表示。）
返回区域的数目。

"""

from typing import List, Optional


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # 每个单元格划分为 4 个三角形区域：0=上, 1=右, 2=下, 3=左
        # 总共 n*n*4 个三角形区域
        parent = list(range(n * n * 4))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for r in range(n):
            for c in range(n):
                idx = (r * n + c) * 4  # 当前单元格的基础索引
                ch = grid[r][c]

                # 根据字符合并内部的三角形区域
                if ch == '/':
                    # '/' 连接上(0)和左(3)，以及右(1)和下(2)
                    union(idx + 0, idx + 3)
                    union(idx + 1, idx + 2)
                elif ch == '\\':
                    # '\' 连接上(0)和右(1)，以及下(2)和左(3)
                    union(idx + 0, idx + 1)
                    union(idx + 2, idx + 3)
                else:
                    # 空格：所有四个三角形都连通
                    union(idx + 0, idx + 1)
                    union(idx + 1, idx + 2)
                    union(idx + 2, idx + 3)

                # 合并与相邻单元格的边
                # 当前单元格的下(2) <-> 下方单元格的上(0)
                if r + 1 < n:
                    union(idx + 2, ((r + 1) * n + c) * 4 + 0)
                # 当前单元格的右(1) <-> 右侧单元格的左(3)
                if c + 1 < n:
                    union(idx + 1, (r * n + c + 1) * 4 + 3)

        # 统计独立连通分量
        regions = set()
        for i in range(n * n * 4):
            regions.add(find(i))

        return len(regions)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将每个 1x1 单元格划分为 4 个三角形区域（上、右、下、左），共计 N*N*4 个区域。
# 使用并查集管理这些区域的连通性：
# 1. 根据单元格内的字符合并内部三角形：
#    - '/' 将上-左合并、右-下合并（分成两半）
#    - '\' 将上-右合并、下-左合并（分成两半）
#    - 空格将四个三角形全部合并
# 2. 合并相邻单元格的边界三角形：
#    - 当前单元格的"下"与下方单元格的"上"合并
#    - 当前单元格的"右"与右侧单元格的"左"合并
# 最终并查集中独立连通分量的数量即为区域数。
#
# 时间复杂度: O(N^2 * α(N^2)) — 每个单元格常数次并查集操作
# 空间复杂度: O(N^2) — 并查集存储 N*N*4 个元素
#
# 关键点:
# - 每个单元格划分为 4 个三角形是核心建模
# - '/' 和 '\' 分别以不同方式分割这 4 个三角形
# - 单元格之间的边界天然需要合并相邻三角形
# - 并查集高效统计连通分量数量
