"""
LeetCode #2745 - Construct the Longest New String
构造最长的新字符串
https://leetcode.cn/problems/construct-the-longest-new-string/

给你三个整数 `x` ，`y` 和 `z` 。
这三个整数表示你有 `x` 个 `"AA"` 字符串，`y` 个 `"BB"` 字符串，和 `z` 个 `"AB"` 字符串。你需要选择这些字符串中的部分字符串（可以全部选择也可以一个都不选择），将它们按顺序连接得到一个新的字符串。新字符串不能包含子字符串 `"AAA"` 或者 `"BBB"` 。
请你返回 新字符串的最大可能长度。
子字符串 是一个字符串中一段连续 非空 的字符序列。

示例 1：
输入：x = 2, y = 5, z = 1 输出：12 解释： 我们可以按顺序连接 "BB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AB" ，得到新字符串 "BBAABBAABBAB" 。 字符串长度为 12 ，无法得到一个更长的符合题目要求的字符串。
示例 2：
输入：x = 3, y = 2, z = 2 输出：14 解释：我们可以按顺序连接 "AB" ，"AB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AA" ，得到新字符串 "ABABAABBAABBAA" 。 字符串长度为 14 ，无法得到一个更长的符合题目要求的字符串。

提示：
`1 <= x, y, z <= 50`
"""

from typing import List, Optional


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return (z + min(x, y) * 2 + (1 if x != y else 0)) * 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Brainteaser, Math, Dynamic Programming
#
# 解题思路:
# "AB" 可以放在任何位置且不产生 "AAA" 或 "BBB"，所以 z 个 "AB" 全部使用。
# "AA" 和 "BB" 需要交替排列以避免连续三个相同字母。最多可以使用 min(x, y)*2 个交替的 "AA" 和 "BB"。
# 如果 x != y，还可以在末尾额外加一个多出来的那种（如 "AA" 或 "BB"）。
# 每个字符串长度为 2，总长度 = 使用的字符串数 * 2。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - "AB" 是万能连接件，不影响 AA/BB 的交替模式
# - AA 和 BB 必须交替出现：AABBAA... 或 BBAABB...
# - 如果 x == y，AA 和 BB 正好交替用完；如果不等，多出的那个可以放最后（多一个）
