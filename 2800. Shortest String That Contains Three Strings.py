"""
LeetCode #2800 - Shortest String That Contains Three Strings
包含三个字符串的最短字符串
https://leetcode.cn/problems/shortest-string-that-contains-three-strings/

给你三个字符串 `a` ，`b` 和 `c` ， 你的任务是找到长度 最短 的字符串，且这三个字符串都是它的 子字符串 。
如果有多个这样的字符串，请你返回 字典序最小 的一个。
请你返回满足题目要求的字符串。
注意：
两个长度相同的字符串 `a` 和 `b` ，如果在第一个不相同的字符处，`a` 的字母在字母表中比 `b` 的字母 靠前 ，那么字符串 `a` 比字符串 `b` 字典序小 。
子字符串 是一个字符串中一段连续的字符序列。

示例 1：
`输入：a` = "abc", `b` = "bca", `c` = "aaa" 输出："aaabca" 解释：字符串 "aaabca" 包含所有三个字符串：a = ans[2...4] ，b = ans[3..5] ，c = ans[0..2] 。结果字符串的长度至少为 6 ，且"aaabca" 是字典序最小的一个。
示例 2：
`输入：a` = "ab", `b` = "ba", `c` = "aba" 输出："aba" 解释：字符串 "aba" 包含所有三个字符串：a = ans[0..1] ，b = ans[1..2] ，c = ans[0..2] 。由于 c 的长度为 3 ，结果字符串的长度至少为 3 。"aba" 是字典序最小的一个。

提示：
`1 <= a.length, b.length, c.length <= 100`
`a` ，`b` ，`c` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s1: str, s2: str) -> str:
            """Merge s2 into s1, overlapping as much as possible."""
            if s2 in s1:
                return s1
            for i in range(min(len(s1), len(s2)), 0, -1):
                if s1[-i:] == s2[:i]:
                    return s1 + s2[i:]
            return s1 + s2

        def solve(x: str, y: str, z: str) -> str:
            return merge(merge(x, y), z)

        import itertools
        strings = [a, b, c]
        best = None
        for perm in itertools.permutations(strings):
            res = solve(*perm)
            if best is None or len(res) < len(best) or (len(res) == len(best) and res < best):
                best = res
        return best



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String, Enumeration
#
# 解题思路:
# 枚举三个字符串的 6 种排列顺序。对于每种顺序，依次合并两个字符串（最大化重叠部分）。
# merge(s1, s2) 将 s2 拼接到 s1 后面，尽可能多地重叠相同的前后缀。
# 在所有结果中取长度最短的，长度相同时取字典序最小的。
#
# 时间复杂度: O(n^2) 其中 n 是字符串长度（每次合并需 O(n^2) 检查重叠）
# 空间复杂度: O(n)
#
# 关键点:
# - 只有 3 个字符串，6 种排列全部枚举即可
# - merge 函数中的重叠检测：从最长重叠开始查找，找到即返回
# - 如果 s2 已经是 s1 的子串，直接返回 s1
