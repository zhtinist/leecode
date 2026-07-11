"""
LeetCode #540 - Single Element in a Sorted Array
中文题名：有序数组中的单一元素
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly
twice, except for one element which appears exactly once. Find this single element that
appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.

【中文翻译】
给定一个有序整数数组，其中每个元素恰好出现两次，只有一个元素恰好出现一次。
找出这个只出现一次的元素。要求 O(log n) 时间复杂度和 O(1) 空间复杂度。

示例 1：
    输入：[1,1,2,3,3,4,4,8,8]
    输出：2

示例 2：
    输入：[3,3,7,7,10,11,11]
    输出：10
"""

from typing import List, Optional


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # Make mid the start of a pair: if mid is odd, move left
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # The single element is to the right of this pair
                left = mid + 2
            else:
                # The single element is to the left (including mid)
                right = mid

        return nums[left]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用二分查找。在单一元素出现之前，成对元素出现在 (偶数, 奇数) 索引位置；
# 在单一元素出现之后，成对元素出现在 (奇数, 偶数) 索引位置。利用这个规律：
# 取中点后先将其对齐到偶数索引（即每一对的第一个位置），比较 nums[mid] 和 nums[mid+1]：
# 若相等，说明单一元素在 mid+2 之后；若不相等，说明单一元素在 mid 或之前。
# 不断缩小区间，最终 left == right 即为答案。
#
# 时间复杂度: O(log N) — 每次迭代将搜索空间减半
# 空间复杂度: O(1) — 仅使用常数个变量
#
# 关键点:
# - 核心规律：单一元素前，成对元素在 (偶, 奇) 位置；单一元素后，在 (奇, 偶) 位置
# - 将 mid 对齐到偶数索引（若为奇数则 mid-1）确保每次比较的是"成对关系的第一个元素"
# - 若 nums[mid] == nums[mid+1] → 单一元素在右边（跳过这一对）
# - 若 nums[mid] != nums[mid+1] → 单一元素在 mid 位置或左边
# - 也可以直接用异或解法 O(N)，但不符合 O(log N) 要求
