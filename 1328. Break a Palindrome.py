"""
LeetCode #1328 - Break a Palindrome
中文题名：破坏回文串
https://leetcode.com/problems/break-a-palindrome/

Given a palindromic string `palindrome`, replace exactly
one character by any lowercase English letter so that the string becomes the
lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return
the empty string.

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"

Example 2:

Input: palindrome = "a"
Output: ""

Constraints:

`1 <= palindrome.length <= 1000`

`palindrome` consists of only lowercase English letters.

【中文翻译】
给定一个回文字符串 `palindrome`，恰好替换一个字符为任意小写英文字母，
使得该字符串变成字典序最小的非回文字符串。

完成替换后，返回最终字符串。如果无法做到，返回空字符串。

示例 1：

输入: palindrome = "abccba"
输出: "aaccba"
解释: 将第一个字符 'b' 替换为 'a'，得到 "aaccba"，这是字典序最小的非回文字符串。

示例 2：

输入: palindrome = "a"
输出: ""
解释: 长度为 1 的字符串无论如何替换都仍是回文串，因此无法得到非回文串。

约束条件：

`1 <= palindrome.length <= 1000`

`palindrome` 仅包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        s = list(palindrome)
        # 遍历前半部分，找到第一个不是 'a' 的字符，替换为 'a'
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return "".join(s)

        # 所有前半部分字符都是 'a'，将最后一个字符改为 'b'
        s[-1] = 'b'
        return "".join(s)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 如果字符串长度为 1，无论怎么替换都还是回文串，直接返回空字符串。
# 2. 将字符串转为列表以便修改。
# 3. 遍历字符串的前半部分（索引 0 到 n//2 - 1）：
#    - 如果当前字符不是 'a'，将其替换为 'a'，这是使字典序最小的最优选择。
#    - 替换后立即返回（因为只需要替换一个字符）。
# 4. 如果前半部分所有字符都是 'a'，则无法通过替换前半部分来破坏回文（替换为 'a'
#    不会改变字符，替换为其他字母只会增大字典序）。此时将最后一个字符改为 'b'，
#    这是破坏回文且字典序最小的方式。
#
# 时间复杂度: O(N) — 最多遍历前半部分字符串一次
# 空间复杂度: O(N) — 将字符串转换为列表
#
# 关键点:
# - 长度为 1 的特殊情况必须返回空字符串
# - 只需遍历前半部分，因为回文串的前半部分决定了字典序
# - 贪心策略：优先替换为 'a'；若全是 'a' 则改最后一个字符为 'b'










