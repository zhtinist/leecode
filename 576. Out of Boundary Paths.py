"""
LeetCode #576 - Out of Boundary Paths
中文题名：出界的路径数
https://leetcode.com/problems/out-of-boundary-paths/

There is an m by n grid with a ball. Given the start coordinate (i,j) of
the ball, you can move the ball to adjacent cell or cross the grid boundary in four
directions (up, down, left, right). However, you can at most move N times.
Find out the number of paths to move the ball out of grid boundary. The answer may be very
large, return it after mod 109 + 7.

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:

Once you move the ball out of boundary, you cannot move it back.

The length and height of the grid is in range [1,50].

N is in range [0,50].

【中文翻译】
有一个 m × n 的网格和一个球。给定球的起始坐标 (i, j)，你可以将球向四个方向（上、下、左、右）
移动到相邻单元格或移出网格边界。但你最多只能移动 N 次。找出将球移出网格边界的路径数量。
答案可能非常大，返回它对 10^9 + 7 取模后的结果。

示例 1：
    输入：m = 2, n = 2, N = 2, i = 0, j = 0
    输出：6

示例 2：
    输入：m = 1, n = 3, N = 3, i = 0, j = 1
    输出：12

注意：
    一旦球出界，不能再移回网格内。
    网格的长度和高度在 [1, 50] 范围内。
    N 在 [0, 50] 范围内。
"""

from typing import List, Optional


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        """
        DP with memoization.
        dp[moves][r][c] = number of ways to go out of bounds from (r, c)
        with remaining 'moves' steps.
        """
        MOD = 10**9 + 7

        from functools import lru_cache

        @lru_cache(None)
        def dp(moves: int, r: int, c: int) -> int:
            # Out of bounds: a valid path
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            # No moves left but still inside: not a valid path
            if moves == 0:
                return 0

            total = 0
            total += dp(moves - 1, r + 1, c)
            total += dp(moves - 1, r - 1, c)
            total += dp(moves - 1, r, c + 1)
            total += dp(moves - 1, r, c - 1)
            return total % MOD

        return dp(maxMove, startRow, startColumn)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用记忆化递归（DP）。定义 dp(k, r, c) 表示从位置 (r, c) 出发、还剩 k 步可走时，
# 走出边界的路径总数。若当前位置已出界，则返回 1（找到一条路径）；若步数为 0 且仍在
# 界内，返回 0。否则向四个方向递归探索，每次步数减 1。使用 lru_cache 避免重复计算。
# 最终答案需对 MOD = 10^9 + 7 取模。
#
# 时间复杂度: O(m * n * maxMove) — 每个状态最多计算一次
# 空间复杂度: O(m * n * maxMove) — memo 缓存大小
#
# 关键点:
# - 递归基：出界返回 1（计入一条路径），步数用完返回 0
# - 每一步都取模确保不溢出
# - 也可自底向上 DP（三维 DP 数组）或滚动数组优化空间
