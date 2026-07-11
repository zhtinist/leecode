"""
LeetCode #1400 - Construct K Palindrome Strings
中文题名：构造 K 个回文串
https://leetcode.com/problems/construct-k-palindrome-strings/

Given a string `s` and an integer `k`. You should construct
`k` non-empty palindrome strings using all the
characters in `s`.

Return True if you can use all the characters in
`s` to construct `k` palindrome strings or
False otherwise.

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

Example 4:

Input: s = "yzyzyzyzyzyzyzy", k = 2
Output: true
Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.

Example 5:

Input: s = "cr", k = 7
Output: false
Explanation: We don't have enough characters in s to construct 7 palindromes.

Constraints:

`1 <= s.length <= 10^5`

All characters in `s` are lower-case English letters.

`1 <= k <= 10^5`

【中文翻译】

给定一个字符串 s 和一个整数 k。你需要使用 s 中的所有字符构造 k 个非空回文串。

如果可以使用 s 中的所有字符构造出 k 个回文串则返回 True，否则返回 False。

示例 1：
输入：s = "annabelle", k = 2
输出：true
解释：可以使用所有字符构造两个回文串，可能的构造方案："anna" + "elble", "anbna" + "elle", "anellena" + "b"

示例 2：
输入：s = "leetcode", k = 3
输出：false
解释：无法使用 s 的所有字符构造 3 个回文串。

示例 3：
输入：s = "true", k = 4
输出：true
解释：唯一的方案是把每个字符单独放在一个字符串中。

示例 4：
输入：s = "yzyzyzyzyzyzyzy", k = 2
输出：true
解释：把所有 z 放在一个字符串，所有 y 放在另一个字符串。两个字符串都是回文串。

示例 5：
输入：s = "cr", k = 7
输出：false
解释：s 中没有足够字符构造 7 个回文串。

约束条件：
1 <= s.length <= 10^5
s 中所有字符均为小写英文字母。
1 <= k <= 10^5
"""

from typing import List, Optional


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # 如果 k > len(s)，无法构造足够的非空回文串
        if k > len(s):
            return False

        # 统计出现奇数次的字符数
        from collections import Counter
        odd_count = sum(1 for v in Counter(s).values() if v % 2 == 1)

        # 每个回文串最多包含一个奇数次字符
        # 因此需要的回文串数至少为 odd_count
        return odd_count <= k



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键观察：
# 1. 每个回文串最多包含一个出现奇数次的字符（位于回文串中心）。
# 2. 因此，如果字符串中奇数频次的字符数为 odd_count，至少需要 odd_count 个回文串。
# 3. 如果可以构造的回文串数范围是 [odd_count, len(s)]。
# 4. 只需检查是否 k >= odd_count 且 k <= len(s)。
#
# 时间复杂度: O(N)  统计字符频次
# 空间复杂度: O(1)  只有 26 个小写字母
#
# 关键点:
# - 回文串的字符频次最多允许一个字符出现奇数次
# - 下限：odd_count（每个奇数次字符需要单独的回文串来容纳）
# - 上限：len(s)（每个字符单独形成一个单字符回文串）
# - 只要 k 在这个范围内即可构造










