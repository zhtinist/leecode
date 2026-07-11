"""
LeetCode #1992 - Find All Groups of Farmland
找到所有的农场组
https://leetcode.cn/problems/find-all-groups-of-farmland/

给你一个下标从 0 开始，大小为 `m x n` 的二进制矩阵 `land` ，其中 `0` 表示一单位的森林土地，`1` 表示一单位的农场土地。
为了让农场保持有序，农场土地之间以矩形的 农场组 的形式存在。每一个农场组都 仅 包含农场土地。且题目保证不会有两个农场组相邻，也就是说一个农场组中的任何一块土地都 不会 与另一个农场组的任何一块土地在四个方向上相邻。
`land` 可以用坐标系统表示，其中 `land` 左上角坐标为 `(0, 0)` ，右下角坐标为 `(m-1, n-1)` 。请你找到所有 农场组 最左上角和最右下角的坐标。一个左上角坐标为 `(r_1, c_1)` 且右下角坐标为 `(r_2, c_2)` 的 农场组 用长度为 4 的数组 `[r_1, c_1, r_2, c_2]` 表示。
请你返回一个二维数组，它包含若干个长度为 4 的子数组，每个子数组表示 `land` 中的一个 农场组 。如果没有任何农场组，请你返回一个空数组。可以以 任意顺序 返回所有农场组。
示例 1：

输入：land = [[1,0,0],[0,1,1],[0,1,1]] 输出：[[0,0,0,0],[1,1,2,2]] 解释： 第一个农场组的左上角为 land[0][0] ，右下角为 land[0][0] 。 第二个农场组的左上角为 land[1][1] ，右下角为 land[2][2] 。
示例 2：

输入：land = [[1,1],[1,1]] 输出：[[0,0,1,1]] 解释： 第一个农场组左上角为 land[0][0] ，右下角为 land[1][1] 。
示例 3：

输入：land = [[0]] 输出：[] 解释： 没有任何农场组。

提示：
`m == land.length`
`n == land[i].length`
`1 <= m, n <= 300`
`land` 只包含 `0` 和 `1` 。
农场组都是 矩形 的形状。
"""

from typing import List, Optional


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        Each farmland group is a rectangle. Find top-left corner (1 with no 1
        above or left), then expand to find bottom-right corner.
        """
        m, n = len(land), len(land[0])
        result = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    # Check if this is the top-left corner of a group
                    if (i > 0 and land[i - 1][j] == 1) or (
                        j > 0 and land[i][j - 1] == 1
                    ):
                        continue

                    # Top-left found, expand to find bottom-right
                    r, c = i, j
                    while r + 1 < m and land[r + 1][j] == 1:
                        r += 1
                    while c + 1 < n and land[i][c + 1] == 1:
                        c += 1

                    result.append([i, j, r, c])

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Array, Matrix
#
# 解题思路:
# 农场组是矩形且互不相邻。识别每个矩形的左上角：
# 一个格子是左上角当且仅当它的上方和左方都不是 1（或越界）。
# 找到左上角后，向右扩展找右边界，向下扩展找下边界，得到右下角坐标。
# 输出 [top, left, bottom, right]。
# 由于题目保证农场组不相邻且是矩形，这种扫描方法正确且高效。
#
# 时间复杂度: O(M * N)，每个格子最多被访问常数次
# 空间复杂度: O(1)，不计输出空间
#
# 关键点:
# - 左上角的判定条件：上方和左方都为 0 或越界
# - 沿行列扩展直接找到右下角
# - 农场组是矩形且不相邻的保证使该方法正确
