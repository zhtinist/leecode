"""
LeetCode #1593 - Split a String Into the Max Number of Unique Substrings
中文题名：拆分字符串使唯一子字符串的数目最大
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/


Given a string `s`, return the maximum number
of unique substrings that the given string can be split into.

You can split string `s` into any list of non-empty
substrings, where the concatenation of the substrings forms the original
string. However, you must split the substrings such that all of them are
unique.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

Constraints:

`1 <= s.length <= 16`

`s` contains only lower case English letters.

【中文翻译】
给定一个字符串 s，将其拆分成若干非空子字符串，要求所有子字符串互不相同。
返回可以得到的最大子字符串数量。

示例 1：输入：s = 'ababccc'
输出：5
解释：拆分为 ['a','b','ab','c','cc']。

示例 2：输入：s = 'aba'
输出：2

示例 3：输入：s = 'aa'
输出：1
"""

from typing import List, Optional


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = 0
        n = len(s)
        def backtrack(start: int, seen: set):
            if start == n:
                self.result = max(self.result, len(seen))
                return
            if len(seen) + (n - start) <= self.result:
                return
            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if sub not in seen:
                    seen.add(sub)
                    backtrack(end, seen)
                    seen.remove(sub)
        backtrack(0, set())
        return self.result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 回溯搜索。从字符串开头开始，尝试切分不同长度的子字符串。
# 使用集合 seen 记录已经使用过的子串。对于每个起始位置，
# 尝试所有可能的结束位置，如果子串未在 seen 中，则加入并递归。
# 剪枝优化：如果当前 seen 大小 + 剩余字符数 < 当前最佳结果，提前返回。
#
# 时间复杂度: O(2^N) 最坏情况，但剪枝使其在实际中很快
# 空间复杂度: O(N) — 递归栈 + 集合
#
# 关键点:
# - 回溯法尝试所有分割方式
# - 剪枝：剩余字符即使全单字符也不够超过当前最优解
# - 使用集合保证子串唯一性












