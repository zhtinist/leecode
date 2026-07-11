"""
LeetCode #1717 - Maximum Score From Removing Substrings
中文题名：删除子字符串的最大得分
https://leetcode.com/problems/maximum-score-from-removing-substrings/

You are given a string `s` and two integers `x` and
`y`. You can perform two types of operations any number of times.

Remove substring `"ab"` and gain `x` points.

For example, when removing `"ab"` from `"cabxbae"`
it becomes `"cxbae"`.

Remove substring `"ba"` and gain `y` points.

For example, when removing `"ba"` from `"cabxbae"`
it becomes `"cabxe"`.

Return the maximum points you can gain after applying the above operations
on `s`.

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:

`1 <= s.length <= 105`

`1 <= x, y <= 104`

`s` consists of lowercase English letters.

【中文翻译】
给定一个字符串 s 和两个整数 x 和 y。每次操作可以删除子字符串 "ab" 并获得 x 分，或删除 "ba" 并获得 y 分。
求可以获得的最大分数。

示例 1：
输入: s = "cdbcbbaaabab", x = 4, y = 5
输出: 19
解释: 删除 "ba"(得5分) → s="cdbcbbaaab"；删除 "ab"(得4分) → s="cdbcbbaa"；再删 "ab"(4分) → "cdbcba"；删 "ba"(5分) → "cdbc"；再删 "ba"。总分=5+4+5+5=19。
"""

from typing import List, Optional


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s: str, first: str, second: str, score: int) -> tuple:
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return ''.join(stack), total

        # 先处理分数高的模式
        if x > y:
            s, score1 = remove_pairs(s, 'a', 'b', x)
            _, score2 = remove_pairs(s, 'b', 'a', y)
        else:
            s, score1 = remove_pairs(s, 'b', 'a', y)
            _, score2 = remove_pairs(s, 'a', 'b', x)

        return score1 + score2
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：总是优先删除分数更高的模式（"ab" 或 "ba"）。
# 使用栈模拟删除过程：遍历字符串，当栈顶和当前字符能组成目标模式时，弹出栈顶并累加分数。
# 处理完高分数模式后，剩余字符串再处理低分数模式。
# 贪心正确性：先删除高分模式不会影响低分模式的总删除数（两种模式不相交）。
#
# 时间复杂度: O(N) — 两次遍历字符串
# 空间复杂度: O(N) — 栈空间
#
# 关键点:
# - 先删除高分模式是关键贪心策略
# - 栈的方法能够一次性找出所有可删除的模式
# - "ab" 和 "ba" 的删除不会相互阻塞
