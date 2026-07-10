"""
LeetCode #219 - Contains Duplicate II
中文题名：存在重复元素 II
https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer *k*, find out whether there are two distinct
indices *i* and *j* in the array such that nums[i] = nums[j] and the absolute
difference between *i* and *j* is at most *k*.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Output: false

【中文翻译】
给定一个整数数组和一个整数 *k*，判断数组中是否存在两个不同的索引 *i* 和 *j*，使得 nums[i] = nums[j] 且 *i* 和 *j* 之间的差的绝对值至多为 *k*。

示例 1：

输入：nums = [1,2,3,1], k = 3
输出：true

示例 2：

输入：nums = [1,0,1,1], k = 1
输出：true

示例 3：

输入：nums = [1,2,3,1,2,3], k = 2
输出：false
"""

from typing import List, Optional


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False












# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用哈希表(字典)记录每个元素最后一次出现的下标。
# 遍历数组，对于当前元素 num：
# - 若 num 已在字典中，且当前下标 i 与上次出现下标之差 <= k，则找到满足条件的重复，返回 True。
# - 否则更新字典中 num 的下标为当前 i。
# 遍历结束后仍未找到，返回 False。
#
# 时间复杂度: O(n) - 遍历数组一次
# 空间复杂度: O(n) - 字典最多存储 n 个元素
#
# 关键点:
# - 只需记录每个元素的最近一次出现位置(下标)，无需存储所有历史位置
# - 滑动窗口思想：字典只保留"有用的"索引信息
# - 也可以使用定长滑动窗口 + Set，当 i > k 时移除 nums[i-k-1]
