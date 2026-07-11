"""
LeetCode #567 - Permutation in String
中文题名：字符串的排列
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2
contains the permutation of s1. In other words, one of the first string's
permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

The input strings only contain lower case letters.

The length of both given strings is in range [1, 10,000].

【中文翻译】
给定两个字符串 s1 和 s2，写一个函数判断 s2 是否包含 s1 的排列。换句话说，第一个字符串的
某一个排列是第二个字符串的子串。

示例 1：
    输入：s1 = "ab", s2 = "eidbaooo"
    输出：True
    解释：s2 包含 s1 的一个排列 ("ba")。

示例 2：
    输入：s1 = "ab", s2 = "eidboaoo"
    输出：False

注意：
    输入的字符串只包含小写字母。
    两个字符串的长度在 [1, 10,000] 范围内。
"""

from typing import List, Optional


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Sliding window with character counts.
        A permutation of s1 exists as a substring of s2 iff some window
        of length |s1| in s2 has identical character frequencies as s1.
        """
        from collections import Counter

        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        target = Counter(s1)
        window = Counter(s2[:len1])

        if window == target:
            return True

        for i in range(len1, len2):
            # Slide the window one character to the right
            left_char = s2[i - len1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            window[s2[i]] += 1

            if window == target:
                return True

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用固定长度的滑动窗口配合字符频率统计。维护一个长度为 |s1| 的窗口在 s2 上滑动，
# 用 Counter 记录窗口内字符频率。如果窗口字符频率与 s1 的字符频率完全一致，则
# 找到了一个 s1 的排列。每次滑动时移除最左侧字符，加入最右侧的新字符，更新窗口频率。
#
# 时间复杂度: O(L1 + L2) — Counter 比较是 O(26) = O(1)，总体为 O(N)
# 空间复杂度: O(1) — Counter 只存储最多 26 个小写字母
#
# 关键点:
# - 窗口长度固定为 s1 的长度，只关心频率是否匹配
# - Counter 的比较是 O(字母表大小) = O(1)
# - 也可以使用长度为 26 的数组代替 Counter，效率更高
