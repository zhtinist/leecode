"""
LeetCode #790 - Domino and Tromino Tiling
中文题名：多米诺和托米诺平铺
https://leetcode.com/problems/domino-and-tromino-tiling/

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These
shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X

Given N, how many ways are there to tile a 2 x N board? Return your answer modulo
10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only
if there are two 4-directionally adjacent cells on the board such that exactly one of the
tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation:
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY

Note:

N  will be in range `[1, 1000]`.

【中文翻译】
我们有两种形状的瓷砖：2×1 的多米诺形状，和 "L" 形的托米诺形状。这些形状可以旋转。

给定 N，有多少种方式可以铺满一个 2×N 的面板？返回答案对 10^9 + 7 取模。

（在平铺中，每个方格都必须被瓷砖覆盖。两个平铺不同，当且仅当面板上存在两个四方向相邻的单元格，使得恰好其中一个平铺中这两个方格被同一块瓷砖占据。）

示例：
输入：3
输出：5
解释：下面列出了五种不同的方式。

注意：

N 的范围是 `[1, 1000]`。
"""

from typing import List, Optional


class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 5

        # dp[n] = number of ways to tile 2 x n board fully
        # dp[n] = 2 * dp[n-1] + dp[n-3]
        dp = [0] * (N + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[N]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。
# 定义两个 DP 状态：
# dp[i][0] = 铺满 2×i 面板的方式数（完全覆盖）
# dp[i][1] = 铺满 2×i 面板但顶部多出一格的方式数（部分覆盖）
# 其中部分覆盖也有两种对称情况（顶部多出或底部多出），但数量相同，用 2*dp[i][1] 表示。
# 状态转移：
# dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2*dp[i-1][1]
# dp[i][1] = dp[i-1][1] + dp[i-2][0]
# 通过代入消元可化简为单状态递推：f[n] = 2*f[n-1] + f[n-3]
# 其中 f(0)=1, f(1)=1, f(2)=2。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N) - 可优化到 O(1) 只存前三个值
#
# 关键点:
# - 两种状态：完全覆盖和部分覆盖
# - 化简后的递推公式 f[n] = 2*f[n-1] + f[n-3]
# - 取模 10^9+7
# - 多米诺可以竖放（覆盖1列）或横放（覆盖2列，需要2个）
# - 托米诺成对使用，形成凸出/凹陷的互补形状
