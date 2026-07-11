"""
LeetCode #266 - Palindrome Permutation
中文题名：回文排列
https://leetcode.com/problems/palindrome-permutation/

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: `"code"`
Output: false

Example 2:

Input: `"aab"`
Output: true

Example 3:

Output: true

【中文翻译】
给定一个字符串，判断其字符能否重新排列形成回文串。

示例 1：

输入：`"code"`
输出：false

示例 2：

输入：`"aab"`
输出：true

示例 3：

输入：`"carerac"`
输出：true
"""

from typing import List, Optional


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter

        char_count = Counter(s)

        # 回文排列条件：最多一个字符出现奇数次
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)

        return odd_count <= 1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: Yes
#
# 解题思路：
# 一个字符串能排列成回文串的充要条件是：最多有一个字符出现奇数次。
# 使用哈希表（Counter）统计每个字符的频率，然后统计出现奇数次的字符个数。
# 如果奇数次的字符 <= 1，返回 True。
#
# 时间复杂度: O(n) — 遍历字符串
# 空间复杂度: O(1) — 字符集大小有限（通常 26 或 128/256）
#
# 关键点：
# - 偶回文：所有字符都出现偶数次
# - 奇回文：恰有一个字符出现奇数次（放在中间）
# - 使用 Counter 或集合追踪奇数状态
