"""
LeetCode #2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
使数组所有元素变成 1 的最少操作次数
https://leetcode.cn/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

给你一个下标从 0 开始的 正 整数数组 `nums` 。你可以对数组执行以下操作 任意 次：
选择一个满足 `0 <= i < n - 1` 的下标 `i` ，将 `nums[i]` 或者 `nums[i+1]` 两者之一替换成它们的最大公约数。
请你返回使数组 `nums` 中所有元素都等于 `1` 的 最少 操作次数。如果无法让数组全部变成 `1` ，请你返回 `-1` 。
两个正整数的最大公约数指的是能整除这两个数的最大正整数。

示例 1：
输入：nums = [2,6,3,4] 输出：4 解释：我们可以执行以下操作： - 选择下标 i = 2 ，将 nums[2] 替换为 gcd(3,4) = 1 ，得到 nums = [2,6,1,4] 。 - 选择下标 i = 1 ，将 nums[1] 替换为 gcd(6,1) = 1 ，得到 nums = [2,1,1,4] 。 - 选择下标 i = 0 ，将 nums[0] 替换为 gcd(2,1) = 1 ，得到 nums = [1,1,1,4] 。 - 选择下标 i = 2 ，将 nums[3] 替换为 gcd(1,4) = 1 ，得到 nums = [1,1,1,1] 。
示例 2：
输入：nums = [2,10,6,14] 输出：-1 解释：无法将所有元素都变成 1 。

提示：
`2 <= nums.length <= 50`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # If there's already a 1, answer = n - count(1)
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        # Find the shortest subarray whose GCD is 1
        min_len = float('inf')
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        if min_len == float('inf'):
            return -1

        # operations = (min_len - 1) to create first 1, + (n - 1) to propagate 1 to all others
        return min_len - 1 + n - 1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Number Theory
#
# 解题思路:
# 如果数组中已有1，答案=n-1的数量（用1去传播到其他元素）。如果没有1，
# 需要找到最短的GCD为1的子数组，用该子数组产生第一个1，然后用这个1传播到全数组。
# 产生第一个1需要len-1次操作，传播到所有元素需要n-1次操作。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(1)
#
# 关键点:
# - 如果全数组的GCD不等于1则返回-1（无法生成1）
# - 先产生一个1（找到最短GCD为1的子数组），再用1传播
# - 传播1到全数组：每次用1和相邻元素做GCD，1次操作传播一个元素
