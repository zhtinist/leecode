"""
LeetCode #1878 - Get Biggest Three Rhombus Sums in a Grid
矩阵中最大的三个菱形和
https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/

给你一个 `m x n` 的整数矩阵 `grid` 。
菱形和 指的是 `grid` 中一个正菱形 边界 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。

注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。
请你按照 降序 返回 `grid` 中三个最大的 互不相同的菱形和 。如果不同的和少于三个，则将它们全部返回。

示例 1：
输入：grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]] 输出：[228,216,211] 解释：最大的三个菱形和如上图所示。 - 蓝色：20 + 3 + 200 + 5 = 228 - 红色：200 + 2 + 10 + 4 = 216 - 绿色：5 + 200 + 4 + 2 = 211
示例 2：
输入：grid = [[1,2,3],[4,5,6],[7,8,9]] 输出：[20,9,8] 解释：最大的三个菱形和如上图所示。 - 蓝色：4 + 2 + 6 + 8 = 20 - 红色：9 （右下角红色的面积为 0 的菱形） - 绿色：8 （下方中央面积为 0 的菱形）
示例 3：
输入：grid = [[7,7,7]] 输出：[7] 解释：所有三个可能的菱形和都相同，所以返回 [7] 。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 100`
`1 <= grid[i][j] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        from heapq import heappush, heappushpop
        m, n = len(grid), len(grid[0])
        top3 = []
        seen = set()

        def add_sum(s: int):
            if s in seen:
                return
            seen.add(s)
            if len(top3) < 3:
                heappush(top3, s)
            elif s > top3[0]:
                heappushpop(top3, s)

        max_size = min(m, n) // 2 + 1

        for i in range(m):
            for j in range(n):
                add_sum(grid[i][j])

                for k in range(1, max_size):
                    top_r, top_c = i, j
                    right_r, right_c = i + k, j + k
                    bottom_r, bottom_c = i + 2 * k, j
                    left_r, left_c = i + k, j - k

                    if (right_r >= m or right_c >= n or
                        bottom_r >= m or bottom_c >= n or
                        left_r >= m or left_c < 0):
                        break

                    s = 0
                    for step in range(k):
                        s += grid[top_r + step][top_c + step]
                    for step in range(k):
                        s += grid[right_r + step][right_c - step]
                    for step in range(k):
                        s += grid[bottom_r - step][bottom_c - step]
                    for step in range(k):
                        s += grid[left_r - step][left_c + step]

                    add_sum(s)

        return sorted(top3, reverse=True)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Matrix, Prefix Sum, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 遍历每个格子作为菱形顶点，尝试不同大小的菱形。
# 1. 菱形可以看作一个旋转45度的正方形，以(i,j)为顶点。
# 2. 对于每个可能的菱形大小k（半边长），计算四个边界上的元素和。
# 3. 使用最小堆维护前三大且互不相同的菱形和。
# 4. 面积为0的菱形（单个格子）也需要考虑。
#
# 时间复杂度: O(m * n * min(m, n)) — 每个格子尝试不同大小
# 空间复杂度: O(1) — 只维护3个值的堆和去重集合
#
# 关键点:
# - 菱形有四个顶点需要边界检查
# - 使用 set 去重，确保返回的是互不相同的和
# - 使用最小堆高效维护前三大值
# - 单个格子（面积为0）也是有效的菱形
