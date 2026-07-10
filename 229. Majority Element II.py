"""
LeetCode #229 - Majority Element II
https://leetcode.com/problems/majority-element-ii/

Given an integer array of size *n*, find all elements that appear more than `&lfloor;
n/3 &rfloor;` times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

from typing import List, Optional


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        if nums.count(cand1) > len(nums) // 3:
            result.append(cand1)
        if cand2 is not None and cand2 != cand1 and nums.count(cand2) > len(nums) // 3:
            result.append(cand2)

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 Boyer-Moore 多数投票算法的扩展版。出现次数超过 n/3 的元素最多有 2 个。
# 第一遍扫描: 维护两个候选人和对应的计数器
# - 如果当前数字等于候选人1: count1++
# - 否则如果等于候选人2: count2++
# - 否则如果 count1==0: 设置候选人1，count1=1
# - 否则如果 count2==0: 设置候选人2，count2=1
# - 否则: count1--, count2-- (三个不同元素两两抵消)
# 第二遍扫描: 验证两个候选人是否真的出现次数超过 n/3 (因为投票只能保证候选人是
# 可能的答案，需要确认)
#
# 时间复杂度: O(n) - 两遍扫描，每遍 O(n)
# 空间复杂度: O(1) - 只使用常量额外空间
#
# 关键点:
# - 超过 n/3 的元素最多 2 个，这是核心前提
# - 抵消逻辑: 三个互不相同的元素可以同时"抵消"(各减一次计数)
# - 第二遍验证必不可少: 第一遍只找出可能的候选人，不保证有效
# - 注意 cand2 可能为 None (只有一个候选人)或 cand2 == cand1 的情况
