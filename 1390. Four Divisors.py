"""
LeetCode #1390 - Four Divisors
中文题名：四因数
https://leetcode.com/problems/four-divisors/

Given an integer array `nums`, return the sum of divisors of the integers
in that array that have exactly four divisors.

If there is no such integer in the array, return `0`.

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Constraints:

`1 <= nums.length <= 10^4`

`1 <= nums[i] <= 10^5`

【中文翻译】

给定一个整数数组 nums，返回其中恰好有四个因数的整数的所有因数之和。如果没有这样的整数，返回 0。

示例 1：
输入：nums = [21,4,7]
输出：32
解释：
21 有 4 个因数：1, 3, 7, 21
4 有 3 个因数：1, 2, 4
7 有 2 个因数：1, 7
答案仅为 21 的因数之和。

约束条件：
1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""

from typing import List, Optional


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            divisors = set()
            i = 1
            while i * i <= num:
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                i += 1
                # 如果已经超过 4 个因数，提前终止
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                total += sum(divisors)

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 遍历每个数字，检查它是否有恰好四个不同的因数。
# 因数判断：从 1 遍历到 sqrt(num)，如果 num % i == 0，
# 则 i 和 num/i 都是因数。
# 如果因数个数超过 4 个则提前终止（优化）。
# 恰好 4 个因数时，累加其和。
#
# 时间复杂度: O(N * sqrt(M))  N 为数组长度，M 为数字最大值
# 空间复杂度: O(1)  每次只存最多 5 个因数
#
# 关键点:
# - 恰好四个因数的数要么是 p^3（p 为质数），要么是两个不同质数的乘积
# - 提前终止：一旦发现超过 4 个因数就不再继续查找
# - 使用 set 存储因数避免重复（完全平方数时 i == num/i）










