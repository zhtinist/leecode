"""
LeetCode #611 - Valid Triangle Number
中文题名：有效三角形的个数
https://leetcode.com/problems/valid-triangle-number/

Given an array consists of non-negative integers, your task is to count the number of triplets
chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:

The length of the given array won't exceed 1000.

The integers in the given array are in the range of [0, 1000].

【中文翻译】
给定一个包含非负整数的数组，你的任务是统计从数组中选取三个数能够组成三角形的三元组的个数。

示例 1：

输入：[2,2,3,4]
输出：3
解释：
有效的组合有：
2,3,4（使用第一个 2）
2,3,4（使用第二个 2）
2,2,3

注意：

给定数组的长度不会超过 1000。

数组中整数的范围为 [0, 1000]。
"""

from typing import List, Optional


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        # Fix the largest side at i, use two pointers for the other two
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # All pairs from left to right-1 combined with 'right' form valid triangles
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 三角形判定条件：两边之和大于第三边，即 a + b > c（其中 c 是最长边）。
# 1. 先对数组排序。
# 2. 固定最长边 i（从右向左扫描），然后使用双指针法在 [0, i-1] 区间内寻找满足
#    nums[left] + nums[right] > nums[i] 的组合。
# 3. 当满足条件时，left 到 right-1 之间的所有元素与 right 组合都满足条件，
#    因为 nums 已排序，左边的元素更小，所以如果 nums[left] + nums[right] > nums[i]，
#    那么 nums[left+1], ..., nums[right-1] 与 nums[right] 也一定满足。
#    因此直接加上 (right - left) 个组合，然后右指针左移。
# 4. 不满足时左指针右移。
#
# 时间复杂度: O(n^2) - 外层 O(n)，内层双指针 O(n)
# 空间复杂度: O(1) - 原地排序不算额外空间，或算 O(log n) 排序栈空间
#
# 关键点:
# - 和 3Sum 类似的双指针技巧
# - 必须排序后才能使用双指针
# - 固定最长边 i，在左边找两小边是关键
# - 当满足条件时一次性累加 (right - left) 个组合
