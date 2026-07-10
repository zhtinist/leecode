"""
LeetCode #258 - Add Digits
中文题名：各位相加
https://leetcode.com/problems/add-digits/

Given a non-negative integer `num`, repeatedly add all its digits until the result
has only one digit.

Example:

Input: `38`
Output: 2
Explanation: The process is like: `3 + 8 = 11`, `1 + 1 = 2`.
Since `2` has only one digit, return it.

Follow up:

Could you do it without any loop/recursion in O(1) runtime?

【中文翻译】
给定一个非负整数 `num`，反复将各位数字相加，直到结果变为一位数字。返回该结果。

示例：

输入：`38`
输出：2
解释：过程如下：`3 + 8 = 11`，`1 + 1 = 2`。
由于 `2` 只有一位数字，返回它。

进阶：

你能否在 O(1) 时间复杂度内、不使用任何循环/递归完成此题？
"""

from typing import List, Optional


class Solution:
    def addDigits(self, num: int) -> int:
        # 数根公式 (Digital Root)
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路：
# 使用数根（Digital Root）数学公式，O(1) 时间和空间。
# 数根 = 1 + (num - 1) % 9，等价于：
# - 如果 num == 0，返回 0
# - 如果 num % 9 == 0，返回 9
# - 否则返回 num % 9
# 原理：一个数与其各位数字之和对 9 同余。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点：
# - 数根公式：dr(n) = 1 + (n - 1) % 9
# - 特殊情况：num = 0 时返回 0
# - 不进位累加的本质是模 9 运算
