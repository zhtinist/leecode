"""
LeetCode #438 - Find All Anagrams in a String
中文题名：找到字符串中所有字母异位词
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of
p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s
and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

【中文翻译】
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20,100。

输出的顺序不重要。

示例 1：

输入：
s: "cbaebabacd"，p: "abc"

输出：
[0, 6]

解释：
起始索引等于 0 的子串是 "cba"，它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac"，它是 "abc" 的字母异位词。

示例 2：

输入：
s: "abab"，p: "ab"

输出：
[0, 1, 2]

解释：
起始索引等于 0 的子串是 "ab"，它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba"，它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab"，它是 "ab" 的字母异位词。
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter()
        result = []
        left = 0

        for right in range(len(s)):
            window_count[s[right]] += 1
            if right - left + 1 > len(p):
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
            if window_count == p_count:
                result.append(left)

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口 + 频率计数器：
# 1. 统计 p 中每个字符的出现频率。
# 2. 使用固定大小的滑动窗口（大小为 len(p)），统计窗口内字符频率。
# 3. 每次右移窗口：添加右边界字符，移除左边界字符（若频率为 0 则删除 key）。
# 4. 当窗口计数与 p_count 相等时，记录当前左边界索引。
# 另一种方式：维护一个 match 计数，当某字符频率与 p 中的频率相等时 match++。
#   当 match == 不同字符种类数时，当前窗口是一个字母异位词。
#
# 时间复杂度: O(n)，n = len(s)，每个字符进出窗口各一次
# 空间复杂度: O(1)，Counter 最多 26 个键
#
# 关键点:
# - 固定大小滑动窗口，大小 = len(p)
# - 比较字典而非重新排序（O(26) vs O(k log k)）
# - 删除频率为 0 的 key 使字典比较更简洁
# - 若 len(p) > len(s)，直接返回空列表
