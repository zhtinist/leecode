"""
LeetCode #2906 - Construct Product Matrix
构造乘积矩阵
https://leetcode.cn/problems/construct-product-matrix/

给你一个下标从 0 开始、大小为 `n * m` 的二维整数矩阵 `grid` ，定义一个下标从 0 开始、大小为 `n * m` 的的二维矩阵 `p`。如果满足以下条件，则称 `p` 为 `grid` 的 乘积矩阵 ：
对于每个元素 `p[i][j]` ，它的值等于除了 `grid[i][j]` 外所有元素的乘积。乘积对 `12345` 取余数。
返回 `grid` 的乘积矩阵。

示例 1：
输入：grid = [[1,2],[3,4]] 输出：[[24,12],[8,6]] 解释：p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24 p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12 p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8 p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6 所以答案是 [[24,12],[8,6]] 。
示例 2：
输入：grid = [[12345],[2],[1]] 输出：[[2],[0],[0]] 解释：p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2 p[1][0] = grid[0][0] * grid[2][0] = 12345 * 1 = 12345. 12345 % 12345 = 0 ，所以 p[1][0] = 0 p[2][0] = grid[0][0] * grid[1][0] = 12345 * 2 = 24690. 24690 % 12345 = 0 ，所以 p[2][0] = 0 所以答案是 [[2],[0],[0]] 。

提示：
`1 <= n == grid.length <= 10^5`
`1 <= m == grid[i].length <= 10^5`
`2 <= n * m <= 10^5`
`1 <= grid[i][j] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        total = n * m
        # Flatten
        flat = [grid[i][j] for i in range(n) for j in range(m)]

        pref = [1] * total
        for i in range(1, total):
            pref[i] = (pref[i - 1] * flat[i - 1]) % MOD

        suff = [1] * total
        for i in range(total - 2, -1, -1):
            suff[i] = (suff[i + 1] * flat[i + 1]) % MOD

        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                res[i][j] = (pref[idx] * suff[idx]) % MOD
        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 将二维矩阵展平为一维数组，计算前缀积和后缀积（均取模 12345）。
# 对于每个位置 (i,j)，其乘积 = 前缀积[idx] * 后缀积[idx] % MOD，即除去自身外所有元素的乘积。
# 这与"除自身外数组的乘积"问题相同，只是扩展到了二维。
#
# 时间复杂度: O(n*m)
# 空间复杂度: O(n*m)
#
# 关键点:
# - 不能用除法（MOD 不是质数），使用前缀积和后缀积
# - 展平矩阵处理，最后重新映射回二维
# - MOD = 12345，所有中间结果取模
