"""
LeetCode #3115 - Maximum Prime Difference
质数的最大距离
https://leetcode.cn/problems/maximum-prime-difference/

给你一个整数数组 `nums`。
返回两个（不一定不同的）质数在 `nums` 中 下标 的 最大距离。

示例 1：

输入： nums = [4,2,9,5,3]
输出： 3
解释： `nums[1]`、`nums[3]` 和 `nums[4]` 是质数。因此答案是 `|4 - 1| = 3`。
示例 2：

输入： nums = [4,8,2,8]
输出： 0
解释： `nums[2]` 是质数。因为只有一个质数，所以答案是 `|2 - 2| = 0`。

提示：
`1 <= nums.length <= 3 * 10^5`
`1 <= nums[i] <= 100`
输入保证 `nums` 中至少有一个质数。
"""

from typing import List, Optional


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        first, last = -1, -1
        for i, x in enumerate(nums):
            if x in primes:
                if first == -1:
                    first = i
                last = i
        return last - first



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Number Theory
#
# 解题思路:
# 由于nums[i] <= 100，可以预先列出100以内的所有质数。遍历数组，
# 记录第一个质数的下标和最后一个质数的下标，它们之间的差值即为最大距离。
# 题目保证至少有一个质数，所以first必定会被赋值。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - nums[i]范围小（<=100），质数集合可硬编码
# - 最大距离一定是最后一个质数下标-第一个质数下标
# - 只有一个质数时距离为0
