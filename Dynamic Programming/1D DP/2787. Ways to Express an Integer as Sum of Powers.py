"""
LeetCode #2787 - Ways to Express an Integer as Sum of Powers
将一个数字表示成幂的和的方案数
https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/

给你两个 正 整数 `n` 和 `x` 。
请你返回将 `n` 表示成一些 互不相同 正整数的 `x` 次幂之和的方案数。换句话说，你需要返回互不相同整数 `[n_1, n_2, ..., n_k]` 的集合数目，满足 `n = n_1^x + n_2^x + ... + n_k^x` 。
由于答案可能非常大，请你将它对 `10^9 + 7` 取余后返回。
比方说，`n = 160` 且 `x = 3` ，一个表示 `n` 的方法是 `n = 2^3 + 3^3 + 5^3`^ 。

示例 1：
输入：n = 10, x = 2 输出：1 解释：我们可以将 n 表示为：n = 3^2 + 1^2 = 10 。 这是唯一将 10 表达成不同整数 2 次方之和的方案。
示例 2：
输入：n = 4, x = 1 输出：2 解释：我们可以将 n 按以下方案表示： - n = 4^1 = 4 。 - n = 3^1 + 1^1 = 4 。

提示：
`1 <= n <= 300`
`1 <= x <= 5`
"""

from typing import List, Optional


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        i = 1
        while True:
            power = i ** x
            if power > n:
                break
            for s in range(n, power - 1, -1):
                dp[s] = (dp[s] + dp[s - power]) % MOD
            i += 1
        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Dynamic Programming
#
# 解题思路:
# 0/1 背包变体。每个整数 i 的 x 次幂只能使用一次（互不相同）。
# 对于每个 power = i^x，从大到小更新 dp[s]（0/1 背包的逆序遍历防止重复使用）。
# dp[s] 表示组成和为 s 的方案数。转移方程：dp[s] += dp[s - power]。
# 直到 power > n 时停止。
#
# 时间复杂度: O(n * k) 其中 k 是满足 i^x <= n 的 i 的个数，n <= 300
# 空间复杂度: O(n)
#
# 关键点:
# - 每个 i^x 只能使用一次，所以是 0/1 背包问题
# - 从大到小遍历 s 确保每个 power 只用一次
# - dp[0] = 1 表示空集和为 0 的一种方案
