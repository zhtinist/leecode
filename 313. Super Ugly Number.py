"""
LeetCode #313 - Super Ugly Number
中文题名：超级丑数
https://leetcode.com/problems/super-ugly-number/

Write a program to find the `nth` super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list
`primes` of size `k`.

Example:

Input: n = 12, `primes` = `[2,7,13,19]`
Output: 32
Explanation: `[1,2,4,7,8,13,14,16,19,26,28,32] `is the sequence of the first 12
super ugly numbers given `primes` = `[2,7,13,19]` of size 4.

Note:

`1` is a super ugly number for any given `primes`.

The given numbers in `primes` are in ascending order.

0 < `k` <= 100, 0 < `n` <= 106, 0 < `primes[i]`
< 1000.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

【中文翻译】
编写一个程序，找出第 n 个超级丑数。

超级丑数是指其所有质因数都是给定质数列表 primes 中的正整数的数。

示例：

输入：n = 12, primes = [2,7,13,19]
输出：32
解释：给定 primes = [2,7,13,19] 大小为 4，前 12 个超级丑数的序列为
[1,2,4,7,8,13,14,16,19,26,28,32]。

注意：

1 是任何给定 primes 的超级丑数。
给定 primes 中的数字按升序排列。
0 < k <= 100, 0 < n <= 10^6, 0 < primes[i] < 1000。
第 n 个超级丑数保证在 32 位有符号整数范围内。
"""

from typing import List, Optional


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k                # k 个指针，每个对应一个质数
        for i in range(1, n):
            # 计算 k 个候选值
            candidates = [ugly[idx[j]] * primes[j] for j in range(k)]
            ugly[i] = min(candidates)
            # 将所有产生该最小值的指针向前移动（去重）
            for j in range(k):
                if ugly[i] == ugly[idx[j]] * primes[j]:
                    idx[j] += 1
        return ugly[-1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划 + 多指针法。这是 #264 Ugly Number II（只有 2,3,5 三个质数）的推广版本。
# 维护 ugly 数组存储已生成的前 i 个超级丑数，ugly[0] = 1。
# 维护 k 个指针 idx[j]，每个指向 ugly 数组中正等待与 primes[j] 相乘的位置。
# 每轮生成下一个丑数时：
# - 对每个质数 primes[j]，计算候选值 ugly[idx[j]] * primes[j]
# - 取所有候选值中的最小值作为下一个丑数 ugly[i]
# - 将所有能产生该最小值的 idx[j] 向前移动（去重，避免重复生成相同的丑数）
#
# 时间复杂度: O(n*k) - 生成 n 个数，每轮扫描 k 个候选值
# 空间复杂度: O(n) - ugly 数组存储 n 个丑数
#
# 关键点:
# - 多指针法是 #264 丑数 II 从 3 个质数推广到 k 个质数
# - 去重是关键：多个 primes[j] 可能产生相同的下一个丑数，所有对应指针都需要 ++
# - 可用最小堆优化到 O(n log k)，但在 k <= 100 时直接扫描也可接受
# - 注意 1 是任何质数集的超级丑数
