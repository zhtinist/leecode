"""
LeetCode #228 - Summary Ranges
https://leetcode.com/problems/summary-ranges/

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""

from typing import List, Optional


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            i += 1
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 线性扫描数组，用一个指针 i 遍历。对于每个起始位置，记录 start = nums[i]，
# 然后不断右移 i 直到下一个数字不连续(nums[i+1] != nums[i] + 1)。
# - 如果 start == nums[i]: 该区间只有一个元素，添加 "start"
# - 否则: 添加 "start->nums[i]"
# i 继续前进处理下一个区间。
#
# 时间复杂度: O(n) - 每个元素访问一次
# 空间复杂度: O(1) - 不计结果数组，只使用常量额外空间
#
# 关键点:
# - 数组已排序且无重复，不需要额外预处理
# - 内层 while 循环将 i 推进到连续区间的末尾
# - 单独一个数字和范围用不同格式表示
# - 可以一次性越过整个连续区间，指针不会回退
