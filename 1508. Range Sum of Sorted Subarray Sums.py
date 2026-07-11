"""
LeetCode #1508 - Range Sum of Sorted Subarray Sums
中文题名：子数组和排序后的区间和
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

Given the array `nums` consisting of `n` positive integers.
You computed the sum of all non-empty continous subarrays from the array and then
sort them in non-decreasing order, creating a new array of `n * (n + 1) / 2` numbers.

Return the sum of the numbers from index `left` to
index `right` (indexed from 1), inclusive, in
the new array. Since the answer can be a huge number return it modulo
10^9 + 7.

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.

Example 2:

Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.

Example 3:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50

Constraints:

`1 <= nums.length <= 10^3`

`nums.length == n`

`1 <= nums[i] <= 100`

`1 <= left <= right <= n * (n + 1) / 2`

【中文翻译】
给定由 n 个正整数组成的数组 nums。计算数组所有非空连续子数组的和，
然后按非递减顺序排序，创建一个包含 n*(n+1)/2 个数字的新数组。
返回新数组中下标从 left 到 right（下标从 1 开始）的数字之和。
由于答案可能很大，返回对 10^9+7 取模的结果。

示例 1：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 5
输出：13
解释：所有子数组和为 [1,3,6,10,2,5,9,3,7,4]。排序后为 [1,2,3,3,4,5,6,7,9,10]。
下标 1 到 5 的和为 1+2+3+3+4=13。

示例 2：

输入：nums = [1,2,3,4], n = 4, left = 3, right = 4
输出：6

示例 3：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
输出：50
"""

from typing import List, Optional


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarray_sums = []
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                subarray_sums.append(cur_sum)
        subarray_sums.sort()
        return sum(subarray_sums[left - 1:right]) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用双重循环枚举所有子数组的和，共 n*(n+1)/2 个。
# 对这些和进行排序，然后取 [left-1, right) 区间的元素求和即可。
# 注意结果对 10^9+7 取模。
#
# 时间复杂度: O(N^2 log N) — N^2 个子数组和需要排序
# 空间复杂度: O(N^2) — 存储所有子数组和
#
# 关键点:
# - 暴力枚举所有子数组和即可，n <= 1000 时 O(N^2) 可行
# - 下标从 1 开始，Python 切片需要注意转换
# - 使用 mod 防止溢出
