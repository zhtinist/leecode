"""
LeetCode #945 - Minimum Increment to Make Array Unique
中文题名：使数组唯一的最小增量
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

Given an array of integers A, a move consists of choosing any `A[i]`, and
incrementing it by `1`.

Return the least number of moves to make every value in `A` unique.

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

【中文翻译】
给定一个整数数组 A，每次操作可以选择任意 A[i] 并将其增加 1。

返回使 A 中的每个值都唯一所需的最少操作次数。

"""

from typing import List, Optional


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        need = 0  # the next available unique number needed

        for num in nums:
            if num < need:
                moves += need - num
                need += 1
            else:
                need = num + 1

        return moves



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 排序数组：先将数组升序排序，这样相等的元素就会相邻排列。
# 2. 贪心处理：维护变量 need 表示下一个可用的最小唯一值。
#    - 如果当前元素 num < need，说明需要增加到 need，操作次数增加 need - num，
#      need 加 1。
#    - 否则（num >= need），无需增加，将 need 设为 num + 1。
# 3. 返回总操作次数。
#
# 时间复杂度: O(N * log N) — 排序的开销。
# 空间复杂度: O(1) — 如果忽略排序的栈空间（或 O(log N) 排序递归栈）。
#
# 关键点:
# - 贪心策略：排序后只需确保每个数不小于前一个数 + 1
# - 追踪"下一个需要的值"而非修改原数组
# - 先排序再贪心是最简洁的做法
