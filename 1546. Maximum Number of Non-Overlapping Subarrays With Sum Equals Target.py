"""
LeetCode #1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
中文题名：和为目标值的最大数目不重叠非空子数组数目
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/


Given an array `nums` and an integer `target`.

Return the maximum number of
non-empty non-overlapping subarrays such that
the sum of values in each subarray is equal to `target`.

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).

Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.

Example 3:

Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3

Example 4:

Input: nums = [0,0,0], target = 0
Output: 3

Constraints:

`1 <= nums.length <= 10^5`

`-10^4 <= nums[i] <= 10^4`

`0 <= target <= 10^6`

【中文翻译】
给定一个数组 nums 和一个整数 target。返回和为 target 的非空不重叠子数组的最大数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 2
输出：2
解释：有 2 个不重叠子数组和为 2：前两个 1 和后两个 1。

示例 2：
输入：nums = [-1,3,5,1,4,2,-9], target = 6
输出：2

示例 3：
输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
输出：3

示例 4：
输入：nums = [0,0,0], target = 0
输出：3
"""

from typing import List, Optional


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            if prefix - target in seen:
                count += 1
                seen = {prefix}
            else:
                seen.add(prefix)
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略。使用哈希集合记录已看到的前缀和。遍历数组，维护当前前缀和 prefix。
# 如果 prefix - target 在集合中，说明找到了一个和为 target 的子数组。
# 由于要求不重叠，找到一个子数组后立即清空集合（只保留当前 prefix），重新开始查找。
# 这保证了选择的是尽可能早结束的子数组，为后续留更多空间。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(N) — 哈希集合
#
# 关键点:
# - 贪心选择最早结束的子数组（最优化不重叠数量）
# - 找到子数组后重置集合，确保不重叠
# - 类似区间调度问题












