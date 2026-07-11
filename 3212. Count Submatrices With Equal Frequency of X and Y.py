"""
LeetCode #3212 - Count Submatrices With Equal Frequency of X and Y
统计 X 和 Y 频数相等的子矩阵数量
https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y/

给你一个二维字符矩阵 `grid`，其中 `grid[i][j]` 可能是 `'X'`、`'Y'` 或 `'.'`，返回满足以下条件的子矩阵数量：
包含 `grid[0][0]`
`'X'` 和 `'Y'` 的频数相等。
至少包含一个 `'X'`。

示例 1：

输入： grid = [["X","Y","."],["Y",".","."]]
输出： 3
解释：

示例 2：

输入： grid = [["X","X"],["X","Y"]]
输出： 0
解释：
不存在满足 `'X'` 和 `'Y'` 频数相等的子矩阵。
示例 3：

输入： grid = [[".","."],[".","."]]
输出： 0
解释：
不存在满足至少包含一个 `'X'` 的子矩阵。

提示：
`1 <= grid.length, grid[i].length <= 1000`
`grid[i][j]` 可能是 `'X'`、`'Y'` 或 `'.'`.
"""

from typing import List, Optional


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        # prefixX[i][j] 和 prefixY[i][j] 表示从 (0,0) 到 (i,j) 的累积
        prefX = [[0] * (n + 1) for _ in range(m + 1)]
        prefY = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefX[i+1][j+1] = prefX[i][j+1] + prefX[i+1][j] - prefX[i][j] + (1 if grid[i][j] == 'X' else 0)
                prefY[i+1][j+1] = prefY[i][j+1] + prefY[i+1][j] - prefY[i][j] + (1 if grid[i][j] == 'Y' else 0)
        for i in range(m):
            for j in range(n):
                x_cnt = prefX[i+1][j+1]
                y_cnt = prefY[i+1][j+1]
                if x_cnt == y_cnt and x_cnt > 0:
                    ans += 1
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 子矩阵必须包含 (0,0)，所以只需枚举所有可能的右下角 (i,j)。
# 使用二维前缀和快速计算每个子矩阵中 X 和 Y 的数量：
# prefX[i+1][j+1] = 区域 (0,0)-(i,j) 中 X 的个数
# 对于每个右下角 (i,j)，检查 X 和 Y 计数是否相等且 X > 0。
#
# 时间复杂度: O(m * n)
# 空间复杂度: O(m * n)
#
# 关键点:
# - 子矩阵必须包含左上角 (0,0)，简化了枚举范围
# - 二维前缀和公式：sum = pref[i+1][j+1] = pref[i][j+1] + pref[i+1][j] - pref[i][j] + val
