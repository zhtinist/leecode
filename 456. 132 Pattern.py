"""
LeetCode #456 - 132 Pattern
中文题名：132 模式
https://leetcode.com/problems/132-pattern/

Given a sequence of n integers a1, a2, ..., an, a 132
pattern is a subsequence ai, aj, ak
such
that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a
132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

【中文翻译】
给定一个由 n 个整数 a1, a2, ..., an 组成的序列，132 模式是指一个子序列 ai, aj, ak，
满足 i < j < k 且 ai < ak < aj。设计一个算法判断列表中是否存在 132 模式。

示例 1：
输入：[1, 2, 3, 4]
输出：False
解释：序列中没有 132 模式。

示例 2：
输入：[3, 1, 4, 2]
输出：True
解释：序列中存在 132 模式：[1, 4, 2]。

示例 3：
输入：[-1, 3, 2, 0]
输出：True
解释：序列中有三个 132 模式：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0]。
"""

from typing import List, Optional


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # third: the "2" in "132" pattern (maximum valid 'ak')
        third = float("-inf")
        stack = []  # monotonic decreasing stack for the "3" values

        # Traverse from right to left, looking for "1" (ai)
        for num in reversed(nums):
            # If current num is smaller than third, we found a "1" (ai < ak)
            if num < third:
                return True
            # While current num is larger than stack top, pop and update third
            while stack and num > stack[-1]:
                third = stack.pop()
            stack.append(num)

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 从右向左遍历，用单调递减栈维护潜在的 "3"（aj）值，用变量 third 记录当前最大的合法 "2"（ak）值。
# 当栈顶元素小于当前 num 时，更新 third 为弹栈的最大值（保证 third < 栈中元素，即 ak < aj）。
# 如果遍历中发现 num < third，说明找到了 i < j < k 且 ai < ak < aj 的 132 模式。
#
# 时间复杂度: O(N) — 每个元素最多入栈出栈一次
# 空间复杂度: O(N) — 单调栈的空间
#
# 关键点:
# - 从右向左遍历，固定思路：找最大的合法 "2"（third）
# - 单调递减栈维护 "3" 候选值
# - third 记录已弹出元素的最大值，保证 third < stack_top
# - 本题也可用前缀最小值 + 有序集合 O(N log N) 解决
