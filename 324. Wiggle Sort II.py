"""
LeetCode #324 - Wiggle Sort II
中文题名：摆动排序 II
https://leetcode.com/problems/wiggle-sort-ii/

Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1]
> nums[2] < nums[3]...`.

Example 1:

Input: `nums = [1, 5, 1, 1, 6, 4]`
Output: One possible answer is `[1, 4, 1, 5, 1, 6]`.

Example 2:

Input: `nums = [1, 3, 2, 2, 3, 1]`
Output: One possible answer is `[2, 3, 1, 3, 1, 2]`.

Note:

You may assume all input has valid answer.

Follow Up:

Can you do it in O(n) time and/or in-place with O(1) extra space?

【中文翻译】
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1：

输入：nums = [1, 5, 1, 1, 6, 4]
输出：一个可能的答案是 [1, 4, 1, 5, 1, 6]。

示例 2：

输入：nums = [1, 3, 2, 2, 3, 1]
输出：一个可能的答案是 [2, 3, 1, 3, 1, 2]。

注意：

你可以假设所有输入都有有效的答案。

进阶：

你能否在 O(n) 时间复杂度和/或 O(1) 空间复杂度内完成？
"""

from typing import List, Optional


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Step 1: Find median using nth_element / sort
        sorted_nums = sorted(nums)
        mid = (n - 1) // 2

        # Step 2: Virtual indexing: A(i) = nums[(2*i + 1) % (n | 1)]
        # Place elements: left half (smaller/equal to median) at odd indices from right
        # right half (larger/equal to median) at even indices from right
        left_idx = mid
        right_idx = n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = sorted_nums[left_idx]
                left_idx -= 1
            else:
                nums[i] = sorted_nums[right_idx]
                right_idx -= 1











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 核心思想：将数组排序后分成两半（较小的一半和较大的一半），然后交错放置。
# 具体做法：
# 1. 对数组排序，找到中位数位置 mid = (n-1)//2
# 2. 将排序后的数组从大到小交错填入：
#    - 较小的一半（索引 0 到 mid）逆序填入偶数位（0, 2, 4, ...）
#    - 较大的一半（索引 mid+1 到 n-1）逆序填入奇数位（1, 3, 5, ...）
# 逆序填入是为了防止相邻相等（如 [4,5,5,6]）。
# 此实现使用 O(n) 额外空间，时间复杂度 O(n log n)。
# 使用快速选择找中位数可优化到 O(n) 时间，使用虚拟索引可实现 O(1) 空间。
#
# 时间复杂度: O(n log n) —— 排序；可优化至 O(n)（快速选择 + 三路分区）
# 空间复杂度: O(n) —— 排序拷贝；可优化至 O(1)（虚拟索引原地交换）
#
# 关键点:
# - 逆序交错放置，防止中位数相邻时相等
# - 较小的一半放偶数索引，较大的一半放奇数索引
# - 进阶：使用 nth_element + virtual indexing 实现 O(n)/O(1)
