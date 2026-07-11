"""
LeetCode #322 - Coin Change
中文题名：零钱兑换
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return
`-1`.

Example 1:

Input: coins = `[1, 2, 5]`, amount = `11`
Output: `3`
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = `[2]`, amount = `3`
Output: -1

Note:

You may assume that you have an infinite number of each kind of coin.

【中文翻译】
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：

输入：coins = [2], amount = 3
输出：-1

注意：

你可以认为每种硬币的数量是无限的。
"""

from typing import List, Optional


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划（完全背包问题）：dp[i] 表示凑成金额 i 所需的最少硬币数。
# 初始化 dp[0] = 0，其余为正无穷（或 amount + 1）。
# 对每种硬币 coin，遍历金额从 coin 到 amount：
#   dp[i] = min(dp[i], dp[i - coin] + 1)
# 使用正序循环（完全背包），因为每种硬币可以无限使用。
# 最后如果 dp[amount] 仍为正无穷，返回 -1；否则返回 dp[amount]。
#
# 时间复杂度: O(amount * n)，n 为硬币种类数
# 空间复杂度: O(amount)
#
# 关键点:
# - 完全背包问题，正序遍历金额
# - dp 初始化为 amount + 1（或 float('inf')），避免溢出
# - 也可以用 BFS 或记忆化搜索，但 DP 是最优解
