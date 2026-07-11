"""
LeetCode #2523 - Closest Prime Numbers in Range
范围内最接近的两个质数
https://leetcode.cn/problems/closest-prime-numbers-in-range/

给你两个正整数 `left` 和 `right` ，请你找到两个整数 `num1` 和 `num2` ，它们满足：
`left <= nums1 < nums2 <= right ` 。
`nums1` 和 `nums2` 都是 质数 。
`nums2 - nums1` 是满足上述条件的质数对中的 最小值 。
请你返回正整数数组 `ans = [nums1, nums2]` 。如果有多个整数对满足上述条件，请你返回 `nums1` 最小的质数对。如果不存在符合题意的质数对，请你返回 `[-1, -1]` 。

示例 1：
输入：left = 10, right = 19 输出：[11,13] 解释：10 到 19 之间的质数为 11 ，13 ，17 和 19 。 质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。 由于 11 比 17 小，我们返回第一个质数对。
示例 2：
输入：left = 4, right = 6 输出：[-1,-1] 解释：给定范围内只有一个质数，所以题目条件无法被满足。

提示：
`1 <= left <= right <= 10^6`
"""

from typing import List, Optional


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(left, right + 1) if is_prime[i]]

        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        ans = [-1, -1]
        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                ans = [primes[i], primes[i + 1]]

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Number Theory
#
# 解题思路:
# 使用埃拉托色尼筛法预先标记[left, right]范围内的所有质数。然后遍历相邻质数对，
# 找到差值最小的一对。若质数不足2个，返回[-1, -1]。
#
# 时间复杂度: O(R log log R + (R-L))，R=right
# 空间复杂度: O(R)
#
# 关键点:
# - 筛法从2筛到sqrt(right)即可标记所有合数
# - 遍历时只需检查[left, right]范围内的质数
# - 由于相邻质数的间距通常很小，遍历质数对效率高
