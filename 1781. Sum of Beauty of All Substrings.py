"""
LeetCode #1781 - Sum of Beauty of All Substrings
中文题名：所有子字符串美丽值之和
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of `"abaacc"` is `3 - 1 = 2`.

Given a string `s`, return the sum of beauty of all of its substrings.

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

Example 2:

Input: s = "aabcbaa"
Output: 17

Constraints:

`1 <= s.length <= 500`

`s` consists of only lowercase English letters.

【中文翻译】
定义一个字符串的美丽值为其中出现频率最高的字符与出现频率最低的字符之间的频率差。
给定字符串 s，返回 s 的所有非空子字符串的美丽值之和。

示例 1：
输入: s = "aabcb"
输出: 5
解释: 美丽值非零的子串：[aab]: max(freq)=2, min=1, 美丽值=1; [aabc]: max=2,min=1, 美丽值=1; [abcb]: max=2,min=1, 美丽值=1; [aabcb]: max=2,min=1, 美丽值=1; [bbc]: max=2,min=1, 美丽值=1。共5。
"""

from typing import List, Optional


class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                max_f = max(freq)
                min_f = min(f for f in freq if f > 0)
                ans += max_f - min_f

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 枚举所有子串的起点 i，向右扩展终点 j，同时维护字符频次数组 freq。
# 对于每个子串，计算 max(freq) - min(freq)（只考虑 freq > 0 的字符）。
# 累加到答案。O(N^2) 对于 s.length <= 500 可接受。
#
# 时间复杂度: O(N^2 * 26) — 每个子串需要 O(26) 计算 max/min
# 空间复杂度: O(1) — 固定的 26 大小频次数组
#
# 关键点:
# - O(N^2) 枚举所有子串
# - 增量更新频次数组避免重新计算
# - min 只考虑出现过的字符（freq > 0）
