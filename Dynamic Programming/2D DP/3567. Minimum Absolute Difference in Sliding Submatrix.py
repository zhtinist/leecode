"""
LeetCode #3567 - Minimum Absolute Difference in Sliding Submatrix
子矩阵的最小绝对差
https://leetcode.cn/problems/minimum-absolute-difference-in-sliding-submatrix/

给你一个 `m x n` 的整数矩阵 `grid` 和一个整数 `k`。
对于矩阵 `grid` 中的每个连续的 `k x k` 子矩阵，计算其中任意两个 不同值 之间的 最小绝对差 。
返回一个大小为 `(m - k + 1) x (n - k + 1)` 的二维数组 `ans`，其中 `ans[i][j]` 表示以 `grid` 中坐标 `(i, j)` 为左上角的子矩阵的最小绝对差。
注意：如果子矩阵中的所有元素都相同，则答案为 0。
子矩阵 `(x1, y1, x2, y2)` 是一个由选择矩阵中所有满足 `x1 <= x <= x2` 且 `y1 <= y <= y2` 的单元格 `matrix[x][y]` 组成的矩阵。

示例 1：

输入： grid = [[1,8],[3,-2]], k = 2
输出： [[2]]
解释：
只有一个可能的 `k x k` 子矩阵：`[[1, 8], [3, -2]]`。
子矩阵中的不同值为 `[1, 8, 3, -2]`。
子矩阵中的最小绝对差为 `|1 - 3| = 2`。因此，答案为 `[[2]]`。
示例 2：

输入： grid = [[3,-1]], k = 1
输出： [[0,0]]
解释：
每个 `k x k` 子矩阵中只有一个不同的元素。
因此，答案为 `[[0, 0]]`。
示例 3：

输入： grid = [[1,-2,3],[2,3,5]], k = 2
输出： [[1,2]]
解释：
有两个可能的 `k × k` 子矩阵：
以 `(0, 0)` 为起点的子矩阵：`[[1, -2], [2, 3]]`。
子矩阵中的不同值为 `[1, -2, 2, 3]`。
子矩阵中的最小绝对差为 `|1 - 2| = 1`。
以 `(0, 1)` 为起点的子矩阵：`[[-2, 3], [3, 5]]`。
子矩阵中的不同值为 `[-2, 3, 5]`。
子矩阵中的最小绝对差为 `|3 - 5| = 2`。
因此，答案为 `[[1, 2]]`。

提示：
`1 <= m == grid.length <= 30`
`1 <= n == grid[i].length <= 30`
`-10^5 <= grid[i][j] <= 10^5`
`1 <= k <= min(m, n)`
"""

from typing import List, Optional


class Solution:
    def minDifference(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = m - k + 1
        cols = n - k + 1
        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # 收集 k×k 子矩阵中的所有元素
                vals = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.append(grid[r][c])

                # 排序后找相邻元素的最小差
                vals.sort()
                min_diff = float('inf')
                for idx in range(1, len(vals)):
                    diff = vals[idx] - vals[idx - 1]
                    if diff < min_diff:
                        min_diff = diff

                ans[i][j] = min_diff if min_diff != float('inf') else 0

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Sorting
#
# 解题思路:
# 由于矩阵规模很小（m, n ≤ 30），可以暴力枚举每个 k×k 子矩阵。
# 对于每个子矩阵：
# 1. 提取子矩阵中的所有 k² 个元素到一个列表中
# 2. 对列表排序
# 3. 遍历排序后的相邻元素对，计算它们之间的绝对差值，取最小值
# 4. 如果子矩阵只有一个元素（k=1），则没有相邻对，答案为 0
# 该方法利用了"任意两个不同值之间的最小绝对差一定出现在排序后相邻的两个元素之间"这一性质。
#
# 时间复杂度: O((m-k+1) * (n-k+1) * k² * log(k²))
# 空间复杂度: O(k²) — 存储单个子矩阵的元素列表
#
# 关键点:
# - 最小值一定在排序后相邻元素之间
# - k=1 时子矩阵只有一个元素，答案为 0
# - 矩阵规模小，暴力枚举完全可行
