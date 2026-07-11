"""
LeetCode #1616 - Split Two Strings to Make Palindrome
中文题名：分割两个字符串得到回文串
https://leetcode.com/problems/split-two-strings-to-make-palindrome/

You are given two strings `a` and `b` of the same length.
Choose an index and split both strings at the same index, splitting
`a` into two strings: `aprefix` and
`asuffix` where `a = aprefix + asuffix`,
and splitting `b` into two strings: `bprefix` and
`bsuffix` where `b = bprefix + bsuffix`.
Check if `aprefix + bsuffix` or
`bprefix + asuffix` forms a palindrome.

When you split a string `s` into `sprefix` and
`ssuffix`, either `ssuffix` or
`sprefix` is allowed to be empty. For example, if `s =
"abc"`, then `"" + "abc"`, `"a" + "bc"`, `"ab"
+ "c"` , and `"abc" + ""` are valid splits.

Return `true` if it is possible to form a palindrome string,
otherwise return `false`.

Notice that `x + y` denotes the concatenation of
strings `x` and `y`.

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.

Example 2:

Input: a = "abdef", b = "fecab"
Output: true

Example 3:

Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

Example 4:

Input: a = "xbdef", b = "xecab"
Output: false

Constraints:

`1 <= a.length, b.length <= 105`

`a.length == b.length`

`a` and `b` consist of lowercase English letters

【中文翻译】
给定两个长度相同的字符串 a 和 b。选择一个下标将两个字符串分割成前缀和后缀：
aprefix + asuffix = a, bprefix + bsuffix = b。
判断是否可以将 aprefix + bsuffix 或 bprefix + asuffix 组成回文字符串。

示例 1：
输入: a = "x", b = "y"
输出: true
解释: aprefix="" + bsuffix="y" = "y"（回文）或 bprefix="" + asuffix="x" = "x"（回文）

示例 2：
输入: a = "abdef", b = "fecab"
输出: true
解释: aprefix="ab" + bsuffix="cab" = "abcab" → 不是回文；bprefix="fe" + asuffix="def" = "fedef" → 是回文
"""

from typing import List, Optional


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_pal(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def check(s1: str, s2: str) -> bool:
            l, r = 0, len(s1) - 1
            while l < r and s1[l] == s2[r]:
                l += 1
                r -= 1
            # 中间剩余部分只需要来自一个字符串就是回文
            return is_pal(s1, l, r) or is_pal(s2, l, r)

        return check(a, b) or check(b, a)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 双指针。前缀来自一个字符串，后缀来自另一个字符串。
# 用双指针从两端向中间匹配（前缀来自 s1，后缀来自 s2），当字符不匹配时停止。
# 此时，中间剩余部分只需要检查其中一个字符串的子串是否是回文即可。
# 因为中间部分全部取自同一个字符串。
# 分别检查 aprefix+bsuffix 和 bprefix+asuffix 两种情况。
#
# 时间复杂度: O(N) — 双指针最多遍历一次
# 空间复杂度: O(1) — 仅使用额外指针
#
# 关键点:
# - 当两端匹配到不相等时，中间部分要么全来自 a 要么全来自 b
# - 需要检查两种拼接方式：a前缀+b后缀 和 b前缀+a后缀
