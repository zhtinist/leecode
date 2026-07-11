"""
LeetCode #2507 - Smallest Value After Replacing With Sum of Prime Factors
使用质因数之和替换后可以取到的最小值
https://leetcode.cn/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

给你一个正整数 `n` 。
请你将 `n` 的值替换为 `n` 的 质因数 之和，重复这一过程。
注意，如果 `n` 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。
返回 `n` 可以取到的最小值。

示例 1：
输入：n = 15 输出：5 解释：最开始，n = 15 。 15 = 3 * 5 ，所以 n 替换为 3 + 5 = 8 。 8 = 2 * 2 * 2 ，所以 n 替换为 2 + 2 + 2 = 6 。 6 = 2 * 3 ，所以 n 替换为 2 + 3 = 5 。 5 是 n 可以取到的最小值。
示例 2：
输入：n = 3 输出：3 解释：最开始，n = 3 。 3 是 n 可以取到的最小值。

提示：
`2 <= n <= 10^5`
"""

from typing import List, Optional


class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_prime_factors(num: int) -> int:
            s = 0
            d = 2
            while d * d <= num:
                while num % d == 0:
                    s += d
                    num //= d
                d += 1
            if num > 1:
                s += num
            return s

        prev = 0
        cur = n
        while cur != prev:
            prev = cur
            cur = sum_prime_factors(cur)
            if cur == prev:  # n is prime, stays same
                break
        return cur



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Number Theory, Simulation
#
# 解题思路:
# 不断将n替换为其质因数之和，直到数值不再变化为止。质因数分解通过从2开始试除法实现，
# 当n为质数时，其质因数之和等于自身，此时循环结束，该值即为最小可能值。
#
# 时间复杂度: O(sqrt(N) * log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 每次替换后数字会变小（除非已经是质数），最终收敛到质数
# - 质因数分解时需重复除以同一个因子（如8=2*2*2，和为6）
# - 最终结果要么是原数（如果已经是质数），要么是约化后的质数
