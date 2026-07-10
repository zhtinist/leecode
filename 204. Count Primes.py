"""
LeetCode #204 - Count Primes
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, *n*.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

from typing import List, Optional


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Sieve of Eratosthenes: only need to check up to sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i as non-prime, start from i*i
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用埃拉托斯特尼筛法（Sieve of Eratosthenes）。
# 1. 创建布尔数组 is_prime[0..n-1]，初始全为 True
# 2. 将 0 和 1 标记为 False（不是质数）
# 3. 从 2 遍历到 sqrt(n)：
#    - 如果 is_prime[i] 为 True，将 i 的所有倍数标记为 False
#    - 从 i*i 开始标记即可（因为小于 i*i 的倍数已被更小的质数标记过）
# 4. 最后统计 is_prime 中 True 的数量
#
# 时间复杂度: O(N log log N) — 筛法的渐进复杂度
# 空间复杂度: O(N) — 布尔数组
#
# 关键点:
# - 外层循环只需到 sqrt(n)
# - 内层从 i*i 开始，避免重复标记
# - 筛法是计数质数的最优解法
