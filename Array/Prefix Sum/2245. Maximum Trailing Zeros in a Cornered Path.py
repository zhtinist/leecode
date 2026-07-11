"""
LeetCode #2245 - Maximum Trailing Zeros in a Cornered Path
转角路径的乘积中最多能有几个尾随零
https://leetcode.cn/problems/maximum-trailing-zeros-in-a-cornered-path/

给你一个二维整数数组 `grid` ，大小为 `m x n`，其中每个单元格都含一个正整数。
转角路径 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 向水平方向 或者 向竖直方向 移动过弯（如果存在弯），而不能访问之前访问过的单元格。在过弯之后，路径应当完全朝 另一个 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；反之亦然。当然，同样不能访问之前已经访问过的单元格。
一条路径的 乘积 定义为：路径上所有值的乘积。
请你从 `grid` 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。
注意：
水平 移动是指向左或右移动。
竖直 移动是指向上或下移动。

示例 1：

输入：grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]] 输出：3 解释：左侧的图展示了一条有效的转角路径。 其乘积为 15 * 20 * 6 * 1 * 10 = 18000 ，共计 3 个尾随零。 可以证明在这条转角路径的乘积中尾随零数目最多。  中间的图不是一条有效的转角路径，因为它有不止一个弯。 右侧的图也不是一条有效的转角路径，因为它需要重复访问已经访问过的单元格。
示例 2：

输入：grid = [[4,3,2],[7,6,1],[8,8,8]] 输出：0 解释：网格如上图所示。 不存在乘积含尾随零的转角路径。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 10^5`
`1 <= m * n <= 10^5`
`1 <= grid[i][j] <= 1000`
"""

from typing import List, Optional


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Helper: count how many times val is divisible by prime p
        def factor_count(val: int, p: int) -> int:
            cnt = 0
            while val % p == 0:
                val //= p
                cnt += 1
            return cnt

        # Precompute factor 2 and factor 5 counts for each cell
        f2 = [[0] * n for _ in range(m)]
        f5 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                f2[i][j] = factor_count(grid[i][j], 2)
                f5[i][j] = factor_count(grid[i][j], 5)

        # Row prefix sums (for left/right queries)
        row2 = [[0] * (n + 1) for _ in range(m)]
        row5 = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row2[i][j + 1] = row2[i][j] + f2[i][j]
                row5[i][j + 1] = row5[i][j] + f5[i][j]

        # Column prefix sums (for up/down queries)
        col2 = [[0] * (m + 1) for _ in range(n)]
        col5 = [[0] * (m + 1) for _ in range(n)]
        for j in range(n):
            for i in range(m):
                col2[j][i + 1] = col2[j][i] + f2[i][j]
                col5[j][i + 1] = col5[j][i] + f5[i][j]

        ans = 0

        for i in range(m):
            for j in range(n):
                # Up segment: from (0, j) to (i, j) inclusive
                up_2 = col2[j][i + 1]
                up_5 = col5[j][i + 1]
                # Down segment: from (i, j) to (m-1, j) inclusive
                down_2 = col2[j][m] - col2[j][i]
                down_5 = col5[j][m] - col5[j][i]
                # Left segment: from (i, 0) to (i, j) inclusive
                left_2 = row2[i][j + 1]
                left_5 = row5[i][j + 1]
                # Right segment: from (i, j) to (i, n-1) inclusive
                right_2 = row2[i][n] - row2[i][j]
                right_5 = row5[i][n] - row5[i][j]

                # Four possible cornered paths (corner cell counted once)
                # Up + Left
                ans = max(ans, min(
                    up_2 + left_2 - f2[i][j],
                    up_5 + left_5 - f5[i][j]
                ))
                # Up + Right
                ans = max(ans, min(
                    up_2 + right_2 - f2[i][j],
                    up_5 + right_5 - f5[i][j]
                ))
                # Down + Left
                ans = max(ans, min(
                    down_2 + left_2 - f2[i][j],
                    down_5 + left_5 - f5[i][j]
                ))
                # Down + Right
                ans = max(ans, min(
                    down_2 + right_2 - f2[i][j],
                    down_5 + right_5 - f5[i][j]
                ))

        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 乘积的尾随零个数 = min(因子2的总数, 因子5的总数)。
# 转角路径最多有一个拐弯，几何上是一条"L形"路径（水平段+竖直段，拐角处重叠一个单元格）。
# 对于任意路径，向边缘延伸只会增加因子2和因子5的计数，因此 min 值不会减少。
# 所以只需考虑从拐角单元格延伸到网格边缘的完整L形路径。
#
# 算法步骤：
# 1. 预处理每个单元格的因子2和因子5的数量。
# 2. 构建行前缀和与列前缀和，支持 O(1) 区间查询。
# 3. 遍历每个单元格作为拐角，考虑四个方向的L形组合：
#    (上+左)、(上+右)、(下+左)、(下+右)，计算每种组合的因子总数，
#    取 min(factor2_total, factor5_total) 作为尾随零个数，更新最大值。
# 4. 拐角单元格在水平和竖直两段中都被计入前缀和，需减去一次。
#
# 时间复杂度: O(m*n) — 每个单元格处理 O(1) 次，前缀和构建 O(m*n)
# 空间复杂度: O(m*n) — 存储因子计数与行/列前缀和
#
# 关键点:
# - 尾随零由因子2和5的最小值决定
# - 向边缘扩展不会减少尾随零，因此只需检查完整延伸到边缘的路径
# - 拐角单元格被两段前缀和重复计算，需要扣除一次
# - 四种L形方向都要检查
