"""
LeetCode #633 - Sum of Square Numbers
中文题名：平方数之和
https://leetcode.com/problems/sum-of-square-numbers/

Given a non-negative integer `c`, your task is to decide whether there're two
integers `a` and `b` such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: 3
Output: False

【中文翻译】
给定一个非负整数 `c`，你的任务是判断是否存在两个整数 `a` 和 `b`，使得 a^2 + b^2 = c。

示例 1：

输入：5
输出：True
解释：1 * 1 + 2 * 2 = 5

示例 2：

输入：3
输出：False
"""

from typing import List, Optional


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)

        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双指针法：判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
# 1. 左指针从 0 开始，右指针从 sqrt(c) 开始。
# 2. 计算 sum = left^2 + right^2。
# 3. 如果 sum == c，返回 True。
# 4. 如果 sum < c，增大 left（因为需要更大的平方和）。
# 5. 如果 sum > c，减小 right（因为需要更小的平方和）。
# 6. 当 left > right 时停止搜索。
#
# 时间复杂度: O(sqrt(c)) - 每个指针最多移动 sqrt(c) 步
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 双指针范围从 [0, sqrt(c)]
# - 注意 a 和 b 可以是相同的数
# - 平方数可能溢出（Python 支持大整数，无此问题）
# - 也可使用费马平方和定理，但双指针更好理解
