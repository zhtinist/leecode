"""
LeetCode #686 - Repeated String Match
中文题名：重复叠加字符串匹配
https://leetcode.com/problems/repeated-string-match/

Given two strings A and B, find the minimum number of times A has to be repeated such that B
is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (&ldquo;abcdabcdabcd&rdquo;), B is a substring
of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:

The length of `A` and `B` will be between 1 and 10000.

【中文翻译】
给定两个字符串 A 和 B，寻找重复叠加字符串 A 的最小次数，使得字符串 B 成为叠加后的字符串的子串。如果不存在这种情况，返回 -1。

例如，A = "abcd"，B = "cdabcdab"。

答案为 3，因为将 A 重复三次后得到 "abcdabcdabcd"，B 是其子串；而 A 重复两次后得到 "abcdabcd"，B 不是其子串。

注意：

`A` 和 `B` 的长度在 1 到 10000 之间。
"""

from typing import List, Optional


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Minimum repeats needed: ceil(len(b) / len(a))
        min_repeats = (len(b) + len(a) - 1) // len(a)
        # Need to check up to min_repeats + 1 in case b straddles the boundary
        for i in range(min_repeats, min_repeats + 2):
            if b in a * i:
                return i
        return -1









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 设 A 长度为 n，B 长度为 m。最少需要重复 ceil(m/n) 次 A 才能使长度 >= m。
# B 最多可能跨两个 A 的边界，所以最多需要检查 ceil(m/n) + 1 次重复。
# 例如 A="abc"，B="cabca"，需要重复 3 次才能使 B 成为子串。
# 因此只需检查 min_repeats 和 min_repeats+1 两种重复次数即可。
#
# 时间复杂度: O(n * (m/n)) = O(m) - 最多生成两个重复串并检查子串
#    或更准确地说，字符串匹配 O(m + len(repeated))。
# 空间复杂度: O(n * (m/n)) = O(m) - 存储重复后的字符串
#
# 关键点:
# - 重复次数的上下界：最少 ceil(m/n)，最多 ceil(m/n) + 1
# - B 可能跨越两个 A 的边界，所以需要检查 min_repeats + 1 次
# - 使用 Python 的 in 操作符检查子串
