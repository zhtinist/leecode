"""
LeetCode #1525 - Number of Good Ways to Split a String
中文题名：字符串的好分割数目
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

You are given a string `s`, a split is called good if
you can split `s` into 2 non-empty strings `p` and
`q` where its concatenation is equal to `s` and the number of
distinct letters in `p` and `q` are the same.

Return the number of good splits you can make in `s`.

Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split `"aacaba"` and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").

Example 3:

Input: s = "aaaaa"
Output: 4
Explanation: All possible splits are good.

Example 4:

Input: s = "acbadbaada"
Output: 2

Constraints:

`s` contains only lowercase English letters.

`1 <= s.length <= 10^5`

【中文翻译】
给定一个字符串 s，如果可以将 s 分割成两个非空字符串 p 和 q（p+q=s），
且 p 和 q 中不同字符的数量相同，则称这是一个"好分割"。
返回 s 中好分割的数量。

示例 1：

输入：s = "aacaba"
输出：2
解释：有 5 种分割方式，其中 2 种是好分割：
("aac", "aba") 左右各 2 个不同字符，
("aaca", "ba") 左右各 2 个不同字符。

示例 2：

输入：s = "abcd"
输出：1

示例 3：

输入：s = "aaaaa"
输出：4
解释：所有可能的分割都是好分割。

示例 4：

输入：s = "acbadbaada"
输出：2
"""

from typing import List, Optional


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        # right_unique[i] = number of unique chars in s[i:]
        right_unique = [0] * (n + 1)
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            right_unique[i] = len(seen)

        left_set = set()
        result = 0
        for i in range(n - 1):
            left_set.add(s[i])
            if len(left_set) == right_unique[i + 1]:
                result += 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 预处理 right_unique[i] 表示 s[i:] 中不同字符的数量（从右往左扫描）。
# 然后从左往右扫描，维护 left_set 记录左半部分的不同字符。
# 对于每个分割点 i（0 <= i < n-1），如果 len(left_set) == right_unique[i+1]，则答案 +1。
#
# 时间复杂度: O(N) — 两次扫描
# 空间复杂度: O(N) — right_unique 数组
#
# 关键点:
# - 预处理右侧信息 + 左侧在线维护
# - 分割点在 i 和 i+1 之间，左半部分是 s[:i+1]，右半部分是 s[i+1:]
# - 无需求出每个位置的完整字符集，只需不同字符数量
