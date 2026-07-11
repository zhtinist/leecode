"""
LeetCode #2521 - Distinct Prime Factors of Product of Array
数组乘积中的不同质因数数目
https://leetcode.cn/problems/distinct-prime-factors-of-product-of-array/

给你一个正整数数组 `nums` ，对 `nums` 所有元素求积之后，找出并返回乘积中 不同质因数 的数目。
注意：
质数 是指大于 `1` 且仅能被 `1` 及自身整除的数字。
如果 `val2 / val1` 是一个整数，则整数 `val1` 是另一个整数 `val2` 的一个因数。

示例 1：
输入：nums = [2,4,3,7,10,6] 输出：4 解释： nums 中所有元素的乘积是：2 * 4 * 3 * 7 * 10 * 6 = 10080 = 2^5 * 3^2 * 5 * 7 。 共有 4 个不同的质因数，所以返回 4 。
示例 2：
输入：nums = [2,4,8,16] 输出：1 解释： nums 中所有元素的乘积是：2 * 4 * 8 * 16 = 1024 = 2^10 。 共有 1 个不同的质因数，所以返回 1 。

提示：
`1 <= nums.length <= 10^4`
`2 <= nums[i] <= 1000`
"""

from typing import List, Optional


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        for num in nums:
            d = 2
            while d * d <= num:
                if num % d == 0:
                    factors.add(d)
                    while num % d == 0:
                        num //= d
                d += 1
            if num > 1:
                factors.add(num)
        return len(factors)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Math, Number Theory
#
# 解题思路:
# 不需要真正计算乘积（会溢出）。对每个数字分别进行质因数分解，将找到的质因数放入集合。
# 每个数的分解通过试除法从2到sqrt(num)进行。最终集合的大小即为不同质因数的数量。
#
# 时间复杂度: O(N * sqrt(M))，N为数组长度，M为最大元素值
# 空间复杂度: O(P)，P为质因数种类数
#
# 关键点:
# - 不需要计算乘积，避免大数溢出
# - 每个数的质因数分解独立进行，结果取并集
# - 试除法对每个因子重复除尽，确保只收集质因数
