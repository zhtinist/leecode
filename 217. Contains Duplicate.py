"""
LeetCode #217 - Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it
should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List, Optional


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)












# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 利用集合(Set)去重。将数组中所有元素放入集合，若集合大小小于原数组长度，
# 则说明存在重复元素，返回 True；否则返回 False。
# 集合基于哈希表实现，插入和查找的平均时间复杂度为 O(1)。
#
# 时间复杂度: O(n) - 遍历数组一次构建集合
# 空间复杂度: O(n) - 集合最多存储 n 个不重复元素
#
# 关键点:
# - Set 的哈希特性使得去重只需 O(n) 时间
# - len(set) < len(list) 是判断重复的最简洁写法
# - 也可用排序后检查相邻元素，但时间为 O(n log n)
