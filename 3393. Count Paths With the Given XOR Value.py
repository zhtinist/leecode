"""
LeetCode #3393 - Count Paths With the Given XOR Value
统计异或值为给定值的路径数目
https://leetcode.cn/problems/count-paths-with-the-given-xor-value/

给你一个大小为 `m x n` 的二维整数数组 `grid` 和一个整数 `k` 。
你的任务是统计满足以下 条件 且从左上格子 `(0, 0)` 出发到达右下格子 `(m - 1, n - 1)` 的路径数目：
每一步你可以向右或者向下走，也就是如果格子存在的话，可以从格子 `(i, j)` 走到格子 `(i, j + 1)` 或者格子 `(i + 1, j)` 。
路径上经过的所有数字 `XOR` 异或值必须 等于 `k` 。
请你返回满足上述条件的路径总数。
由于答案可能很大，请你将答案对 `10^9 + 7` 取余 后返回。

示例 1：

输入：grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11
输出：3
解释：
3 条路径分别为：
`(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2)`
`(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)`
`(0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)`
示例 2：

输入：grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2
输出：5
解释：
5 条路径分别为：
`(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)`
`(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2) → (2, 3)`
`(0, 0) → (1, 0) → (1, 1) → (1, 2) → (1, 3) → (2, 3)`
`(0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2) → (2, 3)`
`(0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2) → (2, 3)`
示例 3：

输入：grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10
输出：0

提示：
`1 <= m == grid.length <= 300`
`1 <= n == grid[r].length <= 300`
`0 <= grid[r][c] < 16`
`0 <= k < 16`
"""

from typing import List, Optional


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        max_xor = 16
        dp = [[[0] * max_xor for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i > 0:
                    for x in range(max_xor):
                        if dp[i - 1][j][x]:
                            dp[i][j][x ^ val] = (dp[i][j][x ^ val] + dp[i - 1][j][x]) % MOD
                if j > 0:
                    for x in range(max_xor):
                        if dp[i][j - 1][x]:
                            dp[i][j][x ^ val] = (dp[i][j][x ^ val] + dp[i][j - 1][x]) % MOD

        return dp[m - 1][n - 1][k]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Dynamic Programming, Matrix
#
# 解题思路:
# 动态规划。dp[i][j][x]表示从(0,0)走到(i,j)且路径XOR值为x的路径数。
# grid值范围<16，所以XOR值范围0-15。dp[i][j][x] = dp[i-1][j][x ^ grid[i][j]] + dp[i][j-1][x ^ grid[i][j]]。
# 最终答案dp[m-1][n-1][k]取模10^9+7。
#
# 时间复杂度: O(m*n*16) = O(m*n)
# 空间复杂度: O(m*n*16) 或 O(n*16) 滚动优化
#
# 关键点:
# - XOR值范围小（<16），所以DP状态空间小
# - 只能向右或向下移动
