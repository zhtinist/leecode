"""
LeetCode #3418 - Maximum Amount of Money Robot Can Earn
机器人可以获得的最大金币数
https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/

给你一个 `m x n` 的网格。一个机器人从网格的左上角 `(0, 0)` 出发，目标是到达网格的右下角 `(m - 1, n - 1)`。在任意时刻，机器人只能向右或向下移动。
网格中的每个单元格包含一个值 `coins[i][j]`：
如果 `coins[i][j] >= 0`，机器人可以获得该单元格的金币。
如果 `coins[i][j] < 0`，机器人会遇到一个强盗，强盗会抢走该单元格数值的 绝对值 的金币。
机器人有一项特殊能力，可以在行程中 最多感化 2个单元格的强盗，从而防止这些单元格的金币被抢走。
注意：机器人的总金币数可以是负数。
返回机器人在路径上可以获得的 最大金币数 。

示例 1：

输入： coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
输出： 8
解释：
一个获得最多金币的最优路径如下：
从 `(0, 0)` 出发，初始金币为 `0`（总金币 = `0`）。
移动到 `(0, 1)`，获得 `1` 枚金币（总金币 = `0 + 1 = 1`）。
移动到 `(1, 1)`，遇到强盗抢走 `2` 枚金币。机器人在此处使用一次感化能力，避免被抢（总金币 = `1`）。
移动到 `(1, 2)`，获得 `3` 枚金币（总金币 = `1 + 3 = 4`）。
移动到 `(2, 2)`，获得 `4` 枚金币（总金币 = `4 + 4 = 8`）。
示例 2：

输入： coins = [[10,10,10],[10,10,10]]
输出： 40
解释：
一个获得最多金币的最优路径如下：
从 `(0, 0)` 出发，初始金币为 `10`（总金币 = `10`）。
移动到 `(0, 1)`，获得 `10` 枚金币（总金币 = `10 + 10 = 20`）。
移动到 `(0, 2)`，再获得 `10` 枚金币（总金币 = `20 + 10 = 30`）。
移动到 `(1, 2)`，获得 `10` 枚金币（总金币 = `30 + 10 = 40`）。

提示：
`m == coins.length`
`n == coins[i].length`
`1 <= m, n <= 500`
`-1000 <= coins[i][j] <= 1000`
"""

from typing import List, Optional


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG = -10 ** 18
        dp = [[[NEG] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                val = coins[i][j]
                for c in range(3):
                    if dp[i][j][c] == NEG:
                        continue
                    # move right
                    if j + 1 < n:
                        nv = dp[i][j][c] + coins[i][j + 1]
                        dp[i][j + 1][c] = max(dp[i][j + 1][c], nv)
                        if c < 2 and coins[i][j + 1] < 0:
                            dp[i][j + 1][c + 1] = max(dp[i][j + 1][c + 1], dp[i][j][c])
                    # move down
                    if i + 1 < m:
                        nv = dp[i][j][c] + coins[i + 1][j]
                        dp[i + 1][j][c] = max(dp[i + 1][j][c], nv)
                        if c < 2 and coins[i + 1][j] < 0:
                            dp[i + 1][j][c + 1] = max(dp[i + 1][j][c + 1], dp[i][j][c])

        return max(dp[m - 1][n - 1])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 三维DP，dp[i][j][c]表示走到(i,j)时使用了c次感化能力的最大金币数。
# 从左上到右下递推，每次只能向右或向下。遇到负数时，可选择使用感化能力（免被抢）或不使用。
# 最多使用2次。最终答案为max(dp[m-1][n-1])。
#
# 时间复杂度: O(m*n*3)
# 空间复杂度: O(m*n*3)
#
# 关键点:
# - 感化能力使负数变为0（不被抢）
# - 最多使用2次能力
# - 机器人金币可为负数
