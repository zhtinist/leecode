"""
LeetCode #581 - Shortest Unsorted Continuous Subarray
中文题名：最短无序连续子数组
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array, you need to find one continuous subarray that if you only sort
this subarray in ascending order, then the whole array will be sorted in ascending order,
too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:

Then length of the input array is in range [1, 10,000].

The input array may contain duplicates, so ascending order here means

【中文翻译】
给定一个整数数组，你需要找到一个连续子数组，如果只将这个子数组升序排序，则整个数组
也将变为升序排序。你需要找到最短的这样的子数组并返回其长度。

示例 1：
    输入：[2, 6, 4, 8, 10, 9, 15]
    输出：5
    解释：你需要将 [6, 4, 8, 10, 9] 升序排序，使整个数组变为升序排序。

注意：
    输入数组的长度在 [1, 10,000] 范围内。
    输入数组可能包含重复元素，因此这里的升序指非递减顺序 (<=)。
"""

from typing import List, Optional


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Two-pass: find the leftmost and rightmost positions where the array is out of order.
        - From left to right, track the running maximum.  The last index where
          nums[i] < running_max is the right boundary of the unsorted segment.
        - From right to left, track the running minimum.  The last index where
          nums[i] > running_min is the left boundary.
        """
        n = len(nums)

        # Find the right boundary
        left, right = n, 0
        cur_max = nums[0]
        for i in range(1, n):
            if nums[i] < cur_max:
                right = i
            else:
                cur_max = nums[i]

        # Find the left boundary
        cur_min = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > cur_min:
                left = i
            else:
                cur_min = nums[i]

        return right - left + 1 if right > left else 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两次线性扫描。从左到右扫描，维护当前已遍历到的最大值 curMax，若 nums[i] 小于
# curMax，说明该位置处于乱序区，更新右边界 right。从右到左扫描，维护当前已遍历到的
# 最小值 curMin，若 nums[i] 大于 curMin，说明该位置处于乱序区，更新左边界 left。
# 最终答案为 right - left + 1（若 right > left，否则整个数组已有序，返回 0）。
#
# 时间复杂度: O(N) — 两次线性扫描
# 空间复杂度: O(1) — 只使用常数额外空间
#
# 关键点:
# - 核心思想：乱序子数组的左边界是最后一个 nums[i] > curMin 的位置，右边界是最后一个
#   nums[i] < curMax 的位置
# - 从左扫描识别哪些位置破坏了"递增"规律；从右扫描识别哪些位置破坏了"递减"规律
# - 也可用排序比较法：排序后对比原数组，找到第一个和最后一个不同位置（O(NlogN)）
