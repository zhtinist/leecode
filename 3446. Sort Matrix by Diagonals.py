"""
LeetCode #3446 - Sort Matrix by Diagonals
按对角线进行矩阵排序
https://leetcode.cn/problems/sort-matrix-by-diagonals/

给你一个大小为 `n x n` 的整数方阵 `grid`。返回一个经过如下调整的矩阵：
左下角三角形（包括中间对角线）的对角线按 非递增顺序 排序。
右上角三角形 的对角线按 非递减顺序 排序。

示例 1：

输入： grid = [[1,7,3],[9,8,2],[4,5,6]]
输出： [[8,2,3],[9,6,7],[4,5,1]]
解释：

标有黑色箭头的对角线（左下角三角形）应按非递增顺序排序：
`[1, 8, 6]` 变为 `[8, 6, 1]`。
`[9, 5]` 和 `[4]` 保持不变。
标有蓝色箭头的对角线（右上角三角形）应按非递减顺序排序：
`[7, 2]` 变为 `[2, 7]`。
`[3]` 保持不变。
示例 2：

输入： grid = [[0,1],[1,2]]
输出： [[2,1],[1,0]]
解释：

标有黑色箭头的对角线必须按非递增顺序排序，因此 `[0, 2]` 变为 `[2, 0]`。其他对角线已经符合要求。
示例 3：

输入： grid = [[1]]
输出： [[1]]
解释：
只有一个元素的对角线已经符合要求，因此无需修改。

提示：
`grid.length == grid[i].length == n`
`1 <= n <= 10`
`-10^5 <= grid[i][j] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # Process each diagonal defined by constant d = i - j
        # d in [-(n-1), n-1]
        for d in range(-(n - 1), n):
            diag = []
            positions = []
            for i in range(n):
                j = i - d
                if 0 <= j < n:
                    diag.append(grid[i][j])
                    positions.append((i, j))

            if d < 0:
                # Top-right triangle: sort non-decreasing (ascending)
                diag.sort()
            else:
                # Bottom-left triangle (including main diagonal):
                # sort non-increasing (descending)
                diag.sort(reverse=True)

            for (i, j), val in zip(positions, diag):
                grid[i][j] = val

        return grid



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Sorting
#
# 解题思路:
# 1. 矩阵对角线由 i - j = d（常数）定义，d 范围 [-(n-1), n-1]
# 2. 对每条对角线提取元素和对应坐标
# 3. d < 0 为右上角三角形对角线，按非递减（升序）排序
# 4. d >= 0 为左下角三角形（含主对角线），按非递增（降序）排序
# 5. 将排序后的值按坐标填回矩阵
#
# 时间复杂度: O(n^2 * log n) — 每条对角线排序，总元素 n^2
# 空间复杂度: O(n) — 每条对角线的临时数组
#
# 关键点:
# - 对角线标识为 i - j，主对角线 d=0
# - 右上角 (d < 0) 升序，左下角 (d >= 0) 降序
