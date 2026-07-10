"""
LeetCode #287 - Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Given an array *nums* containing *n* + 1 integers where each integer is between 1
and *n* (inclusive), prove that at least one duplicate number must exist. Assume that
there is only one duplicate number, find the duplicate one.

Example 1:

Input: `[1,3,4,2,2]`
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

You must not modify the array (assume the array is read only).

You must use only constant, *O*(1) extra space.

Your runtime complexity should be less than *O*(*n*^2).

There is only one duplicate number in the array, but it could be repeated more than
once.
"""

from typing import List, Optional


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Find the duplicate number using Floyd's Cycle Detection.

        Treat the array as a linked list where nums[i] points to nums[nums[i]].
        Since there's a duplicate, there must be a cycle.
        Phase 1: Find intersection point of slow and fast pointers.
        Phase 2: Find the entrance of the cycle (the duplicate).
        """
        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find cycle entrance
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用弗洛伊德的循环检测算法（Floyd's Cycle Detection / 龟兔赛跑）。
# 将数组视为一个隐式链表：nums[i] 表示从索引 i 指向索引 nums[i] 的边。
# 由于有重复数字，意味着至少有两个索引指向同一个值，形成了环。
#
# 第一阶段：快慢指针。slow 每次走一步 (nums[slow])，fast 每次走两步
# (nums[nums[fast]])。它们会在环内某点相遇。
#
# 第二阶段：找环入口。将 slow 重置到起点 (nums[0])，fast 留在相遇点。
# 两个指针都以步长 1 前进，再次相遇的点就是环的入口，即重复数字。
#
# 时间复杂度: O(N) - 两个阶段各需要 O(N)
# 空间复杂度: O(1) - 只使用两个指针
#
# 关键点:
# - 不修改数组 + O(1) 空间 + O(N) 时间 — 只能用龟兔赛跑
# - 将数组视作链表是关键思维转换
# - 环的入口就是重复数字
# - 也可以用二分查找法（O(N log N) 时间，O(1) 空间）
