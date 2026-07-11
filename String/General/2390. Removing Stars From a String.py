"""
LeetCode #2390 - Removing Stars From a String
从字符串中移除星号
https://leetcode.cn/problems/removing-stars-from-a-string/

给你一个包含若干星号 `*` 的字符串 `s` 。
在一步操作中，你可以：
选中 `s` 中的一个星号。
移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。
返回移除 所有 星号之后的字符串。
注意：
生成的输入保证总是可以执行题面中描述的操作。
可以证明结果字符串是唯一的。

示例 1：
输入：s = "leet**cod*e" 输出："lecoe" 解释：从左到右执行移除操作： - 距离第 1 个星号最近的字符是 "leet**cod*e" 中的 't' ，s 变为 "lee*cod*e" 。 - 距离第 2 个星号最近的字符是 "lee*cod*e" 中的 'e' ，s 变为 "lecod*e" 。 - 距离第 3 个星号最近的字符是 "lecod*e" 中的 'd' ，s 变为 "lecoe" 。 不存在其他星号，返回 "lecoe" 。
示例 2：
输入：s = "erase*****" 输出："" 解释：整个字符串都会被移除，所以返回空字符串。

提示：
`1 <= s.length <= 10^5`
`s` 由小写英文字母和星号 `*` 组成
`s` 可以执行上述操作
"""

from typing import List, Optional


class Solution:
    def removeStars(self, s: str) -> str:
        """
        Use a stack: push non-star characters; pop when a star is encountered.
        The stack simulates the removal of the closest non-star character
        to the left of each star.
        """
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
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
# 1. 使用栈模拟操作：遍历字符串，遇到非星号字符时压入栈，遇到星号(*)时弹出栈顶元素。
# 2. 栈顶元素恰好是当前星号左侧最近的非星号字符，完美模拟题目描述的移除操作。
# 3. 遍历结束后，栈中剩余字符即为最终结果。
#
# 时间复杂度: O(n) — 每个字符入栈/出栈一次
# 空间复杂度: O(n) — 栈中最多存储所有非星号字符
#
# 关键点:
# - 栈是最直接的数据结构，天然匹配"删除最近字符"的语义
# - 题目保证操作总是可执行的（遇到星号时栈非空）
