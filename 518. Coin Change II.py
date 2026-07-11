"""
LeetCode #518 - Coin Change II
中文题名：零钱兑换 II
https://leetcode.com/problems/coin-change-ii/

You are given coins of different denominations and a total amount of money. Write a function
to compute the number of combinations that make up that amount. You may assume that you have
infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1

Note:

You can assume that

0 <= amount <= 5000

1 <= coin <= 5000

the number of coins is less than 500

the answer is guaranteed to fit into signed 32-bit integer

【中文翻译】
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
假设每一种面额的硬币有无限个。

示例 1：

输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2：

输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3。

示例 3：

输入：amount = 10, coins = [10]
输出：1

注意：

你可以假设：

0 <= amount <= 5000

1 <= coin <= 5000

硬币种类数小于 500

答案保证可以存入 32 位有符号整数
"""

from typing import List, Optional


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划（完全背包求组合数）：dp[i] 表示凑成金额 i 的硬币组合数。
# 初始化 dp[0] = 1（凑成金额 0 有一种方式：不使用任何硬币）。
# 外层遍历每种硬币，内层正序遍历金额（完全背包）：
#   dp[i] += dp[i - coin]
# 外层遍历硬币保证组合不考虑顺序（组合数而非排列数）。
# 若改为外层遍历金额、内层遍历硬币，则计算的是排列数。
# 最后返回 dp[amount]。
#
# 时间复杂度: O(amount * n)，n 为硬币种类数
# 空间复杂度: O(amount)
#
# 关键点:
# - 完全背包问题，正序遍历金额
# - 外层硬币、内层金额的顺序保证是组合数而非排列数
# - dp[0] = 1 是基础情况
# - 与 #322 零钱兑换的区别：求组合数 vs 求最少硬币数
