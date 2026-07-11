"""
LeetCode #3561 - Resulting String After Adjacent Removals
移除相邻字符
https://leetcode.cn/problems/resulting-string-after-adjacent-removals/

给你一个由小写英文字母组成的字符串 `s`。
你 必须 在字符串 `s` 中至少存在两个 连续 字符时，反复执行以下操作：
移除字符串中 最左边 的一对按照字母表 连续 的相邻字符（无论是按顺序还是逆序，例如 `'a'` 和 `'b'`，或 `'b'` 和 `'a'`）。
将剩余字符向左移动以填补空隙。
当无法再执行任何操作时，返回最终的字符串。
注意：字母表是循环的，因此 `'a'` 和 `'z'` 也视为连续。

示例 1：

输入: s = "abc"
输出: "c"
解释:
从字符串中移除 `"ab"`，剩下 `"c"`。
无法进行进一步操作。因此，所有可能移除操作后的最终字符串为 `"c"`。
示例 2：

输入: s = "adcb"
输出: ""
解释:
从字符串中移除 `"dc"`，剩下 `"ab"`。
从字符串中移除 `"ab"`，剩下 `""`。
无法进行进一步操作。因此，所有可能移除操作后的最终字符串为 `""`。
示例 3：

输入: s = "zadb"
输出: "db"
解释:
从字符串中移除 `"za"`，剩下 `"db"`。
无法进行进一步操作。因此，所有可能移除操作后的最终字符串为 `"db"`。

提示:
`1 <= s.length <= 10^5`
`s` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        def is_consecutive(a: str, b: str) -> bool:
            """Check if two lowercase letters are alphabetically consecutive (cyclic)."""
            diff = abs(ord(a) - ord(b))
            return diff == 1 or diff == 25  # diff=25 covers 'a' & 'z'

        for ch in s:
            if stack and is_consecutive(stack[-1], ch):
                stack.pop()  # remove the leftmost consecutive pair
            else:
                stack.append(ch)

        return ''.join(stack)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, String, Simulation
#
# 解题思路:
# 使用栈模拟整个过程。从左到右遍历字符串，对于每个字符：
# 检查栈顶元素与当前字符是否构成"字母表连续"的关系（差值为 1，或 'a' 和 'z' 之间差值为 25）。
# 如果是，说明栈顶和当前字符构成最左边连续对，将栈顶弹出（移除该对）。
# 否则，将当前字符压入栈中。
# 遍历结束后栈中剩余字符即为最终结果。
#
# 时间复杂度: O(n)，每个字符最多入栈和出栈各一次。
# 空间复杂度: O(n)，栈最多存储所有未移除的字符。
#
# 关键点:
# - 栈的自然后进先出特性恰好匹配"移除后左边字符与右边字符相邻"的规则。
# - 字母表是循环的，所以 'a' 和 'z' 也视为连续（差值 25）。
# - 每次检查栈顶与当前字符，等价于不断找最左边连续对并移除。
