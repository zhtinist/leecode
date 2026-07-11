"""
LeetCode #2556 - Disconnect Path in a Binary Matrix by at Most One Flip
二进制矩阵中翻转最多一次使路径不连通
https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

给你一个下标从 0 开始的 `m x n` 二进制 矩阵 `grid` 。你可以从一个格子 `(row, col)` 移动到格子 `(row + 1, col)` 或者 `(row, col + 1)` ，前提是前往的格子值为 `1` 。如果从 `(0, 0)` 到 `(m - 1, n - 1)` 没有任何路径，我们称该矩阵是 不连通 的。
你可以翻转 最多一个 格子的值（也可以不翻转）。你 不能翻转 格子 `(0, 0)` 和 `(m - 1, n - 1)` 。
如果可以使矩阵不连通，请你返回 `true` ，否则返回 `false` 。
注意 ，翻转一个格子的值，可以使它的值从 `0` 变 `1` ，或从 `1` 变 `0` 。

示例 1：

输入：grid = [[1,1,1],[1,0,0],[1,1,1]] 输出：true 解释：按照上图所示我们翻转蓝色格子里的值，翻转后从 (0, 0) 到 (2, 2) 没有路径。
示例 2：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]] 输出：false 解释：无法翻转至多一个格子，使 (0, 0) 到 (2, 2) 没有路径。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 1000`
`1 <= m * n <= 10^5`
`grid[0][0] == grid[m - 1][n - 1] == 1`
"""

from typing import List, Optional


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9

        # forward DP: number of ways to reach (i,j) from (0,0)
        fw1 = [[0] * n for _ in range(m)]
        fw2 = [[0] * n for _ in range(m)]
        fw1[0][0] = fw2[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i == 0 and j == 0):
                    continue
                if i > 0:
                    fw1[i][j] = (fw1[i][j] + fw1[i-1][j]) % MOD1
                    fw2[i][j] = (fw2[i][j] + fw2[i-1][j]) % MOD2
                if j > 0:
                    fw1[i][j] = (fw1[i][j] + fw1[i][j-1]) % MOD1
                    fw2[i][j] = (fw2[i][j] + fw2[i][j-1]) % MOD2

        total1 = fw1[m-1][n-1]
        total2 = fw2[m-1][n-1]
        if total1 == 0:
            return True  # already disconnected

        # backward DP: number of ways to reach (m-1,n-1) from (i,j)
        bw1 = [[0] * n for _ in range(m)]
        bw2 = [[0] * n for _ in range(m)]
        bw1[m-1][n-1] = bw2[m-1][n-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0 or (i == m - 1 and j == n - 1):
                    continue
                if i + 1 < m:
                    bw1[i][j] = (bw1[i][j] + bw1[i+1][j]) % MOD1
                    bw2[i][j] = (bw2[i][j] + bw2[i+1][j]) % MOD2
                if j + 1 < n:
                    bw1[i][j] = (bw1[i][j] + bw1[i][j+1]) % MOD1
                    bw2[i][j] = (bw2[i][j] + bw2[i][j+1]) % MOD2

        # count critical cells (on all paths) excluding start and end
        critical = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or (i == m - 1 and j == n - 1):
                    continue
                if grid[i][j] == 0:
                    continue
                if (fw1[i][j] * bw1[i][j]) % MOD1 == total1 and \
                   (fw2[i][j] * bw2[i][j]) % MOD2 == total2:
                    critical += 1
                    if critical > 1:
                        return False

        return True  # 0 or 1 critical cells



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Array, Dynamic Programming, Matrix
#
# 解题思路:
# 通过DP计算从起点到每个格子的路径数（正向）和从每个格子到终点的路径数（反向）。
# 若一个格子在所有路径上，则正反向路径数乘积等于总路径数。如果这样的关键格子（排除首尾）
# 不超过1个，则翻转一个就能断开所有路径。使用双模数避免大数溢出和哈希冲突。
#
# 时间复杂度: O(M*N)
# 空间复杂度: O(M*N)
#
# 关键点:
# - 关键格子=正反向路径数乘积==总路径数的格子（排除首尾）
# - 双模数避免哈希冲突（单一模数可能误判）
# - 若路径数为0则已经断开，直接返回True
# - 翻转1->0破坏关键格子，0->1无法帮助断开
