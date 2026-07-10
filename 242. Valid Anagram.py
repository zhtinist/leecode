"""
LeetCode #242 - Valid Anagram
中文题名：有效的字母异位词
https://leetcode.com/problems/valid-anagram/

Given two strings *s* and *t *, write a function to determine if
*t* is an anagram of *s*.

Example 1:

Input: *s* = "anagram", *t* = "nagaram"
Output: true

Example 2:

Input: *s* = "rat", *t* = "car"
Output: false

Note:

You may assume the string contains only lowercase alphabets.

Follow up:

What if the inputs contain unicode characters? How would you adapt your solution to such
case?

【中文翻译】
给定两个字符串 *s* 和 *t*，编写一个函数来判断 *t* 是否是 *s* 的字母异位词。

示例 1：

输入：*s* = "anagram", *t* = "nagaram"
输出：true

示例 2：

输入：*s* = "rat", *t* = "car"
输出：false

注意：

你可以假设字符串只包含小写字母。

进阶：

如果输入包含 Unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""

from typing import List, Optional


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 长度不等一定不是异位词
        if len(s) != len(t):
            return False

        # 使用长度为 26 的数组统计字符频率（仅小写字母）
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # 如果所有计数归零，则是异位词
        return all(c == 0 for c in count)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路：
# 使用字符计数法。因为题目限定只有小写字母，可以用一个长度为 26 的数组
# 记录每个字符在 s 中出现的次数减去在 t 中出现的次数。最后检查所有计数
# 是否为零。如果包含 Unicode 字符，可将数组换成字典（HashMap）即可。
#
# 时间复杂度: O(n) — 遍历两个字符串各一次
# 空间复杂度: O(1) — 固定大小 26 的数组（若 Unicode 则为 O(k)，k=字符集大小）
#
# 关键点：
# - 先判断长度是否相等
# - 一次遍历同时处理 s 和 t
# - Follow up: 用字典替代数组即可处理 Unicode
