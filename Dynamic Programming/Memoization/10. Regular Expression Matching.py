"""
LeetCode #10 - Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

Given an input string s and a pattern p, implement regular expression matching
with support for '.' and '*' where:

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'.
                 Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be
    a previous valid character to match.

================================================================================
解题思路 / Approach
================================================================================
核心难点 / Core difficulty:
    s 和 p 不能按下标一一对齐。因为 "a*" 可以匹配 0 个、1 个或多个 'a',
    所以 s 的第 i 个字符不一定对应 p 的第 i 个字符。
    s and p cannot be aligned by the same index. "a*" may consume 0/1/many
    chars in s, so s[i] does not always pair with p[i].

算法 / Algorithm:
    记忆化递归（自顶向下 DP)/ Memoized recursion (top-down DP)
    子问题 dfs(i, j) = s[i:] 能否匹配 p[j:] ?
    Subproblem: dfs(i, j) = whether s[i:] matches p[j:]

    状态数 / States: (i, j) 最多 len(s) * len(p) 种 → O(m * n)
    @cache 保证每个状态只算一次 / each state is computed once
================================================================================
"""

from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 入口：从 s[0] 和 p[0] 开始匹配
        # Entry point: match from the beginning of s and p
        return self.match(s, p)

    def char_matches(self, s_char: str, p_char: str) -> bool:
        """
        判断单个字符是否匹配 / Check single-char match
        - 普通字母：必须相同 / same letter required
        - '.'：匹配任意一个字符 / matches any one character
        """
        return s_char == p_char or p_char == '.'

    def match(self, s: str, p: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            """
            dfs(i, j): s 从下标 i 开始的后缀，能否匹配 p 从下标 j 开始的后缀
            dfs(i, j): can suffix s[i:] match suffix p[j:]?
            """

            # ── Base case / 边界条件 ──────────────────────────────────────
            # pattern 用完了 → 只有 s 也刚好用完才算成功
            # Pattern exhausted → match succeeds only if s is also exhausted
            if j == len(p):
                return i == len(s)

            # ── Case A: 当前 pattern 形如 "x*" / pattern looks like "x*" ───
            # 判断方式：看 p[j+1] 是不是 '*'（'*' 永远修饰它前面的字符）
            # Detect by checking p[j+1] == '*' ('*' always modifies the char before it)
            #
            # 例 / e.g. p = "a*b", j=0 → p[0]='a', p[1]='*' → 当前是 "a*"
            if j + 1 < len(p) and p[j + 1] == '*':
                # 选择 1 / Choice 1: '*' 匹配 0 次 → 跳过 "x*" 两个字符
                # '*' matches 0 times → skip both "x" and "*", go to dfs(i, j+2)
                #
                # 例 / e.g. s="aab", p="c*a*b", j=0 ("c*")
                #       c* 匹配 0 次 c → 直接看后面的 pattern
                choice_zero = dfs(i, j + 2)

                # 选择 2 / Choice 2: '*' 匹配 1 次或多次
                # 先让 s[i] 和 x 匹配，s 前进一位，p 停在 j（'*' 还能继续用）
                # Match s[i] with x once, advance i, keep j (the "x*" can still repeat)
                #
                # 例 / e.g. s="aa", p="a*", j=0
                #       第一次用 a* 吃掉 s[0]='a' → dfs(1, 0)
                #       第二次继续用 a* 吃掉 s[1]='a' → dfs(2, 0)
                #       最后 a* 匹配 0 次 → dfs(2, 2) → True
                #
                # 注意 / Note: i < len(s) 防止 s 用完还访问 s[i]
                # guard against IndexError when s is already exhausted
                choice_one_or_more = (
                    i < len(s)
                    and self.char_matches(s[i], p[j])
                    and dfs(i + 1, j)
                )

                # 两种选择有一个成立即可 / either choice succeeding is enough
                return choice_zero or choice_one_or_more

            # ── Case B: 普通字符或 '.' / normal char or '.' ─────────────────
            # 没有 '*'，s[i] 必须和 p[j] 匹配，然后双方各前进一位
            # No '*': s[i] must match p[j], then both pointers move forward
            #
            # 例 / e.g. s="ab", p="ab", j=0 → match 'a' → dfs(1,1) → match 'b' → dfs(2,2) → True
            #
            # s 用完了但 pattern 还有普通字符 → 无法匹配 → 短路为 False
            # If s is exhausted but pattern still has normal chars → False
            return (
                i < len(s)
                and self.char_matches(s[i], p[j])
                and dfs(i + 1, j + 1)
            )

        # 从整个 s 和整个 p 开始 / start matching full s against full p
        return dfs(0, 0)
