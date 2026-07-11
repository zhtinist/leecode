"""
LeetCode #267 - Palindrome Permutation II
中文题名：回文排列 II
https://leetcode.com/problems/palindrome-permutation-ii/

Given a string `s`, return all the palindromic permutations (without duplicates)
of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: `"aabb"`
Output: `["abba", "baab"]`

Example 2:

Input: `"abc"`
Output: `[]`

【中文翻译】
给定一个字符串 `s`，返回其所有可能的回文排列（不含重复）。如果无法形成任何回文排列，返回空列表。

示例 1：

输入：`"aabb"`
输出：`["abba", "baab"]`

示例 2：

输入：`"abc"`
输出：`[]`
"""

from typing import List, Optional


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        from collections import Counter

        char_count = Counter(s)

        # 检查是否可能构成回文
        odd_chars = [ch for ch, cnt in char_count.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return []

        # 构建一半的字符列表（每个字符取 count//2 个）
        half_chars = []
        mid_char = ""
        for ch, cnt in char_count.items():
            half_chars.extend([ch] * (cnt // 2))
            if cnt % 2 == 1:
                mid_char = ch

        half_chars.sort()
        res = []
        used = [False] * len(half_chars)

        def backtrack(path):
            if len(path) == len(half_chars):
                left = ''.join(path)
                res.append(left + mid_char + left[::-1])
                return

            for i in range(len(half_chars)):
                if used[i]:
                    continue
                # 跳过重复字符以避免重复排列
                if i > 0 and half_chars[i] == half_chars[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(half_chars[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 1. 先统计字符频率，检查是否可能构成回文（奇数频次字符 <= 1）。
# 2. 取出每个字符的一半数量（count//2），构建"左半部分"字符列表。
# 3. 如果有奇数频次字符，作为中间字符 mid。
# 4. 对半部分字符列表进行回溯生成所有不重复排列。
# 5. 每个排列拼接为: 左半 + mid + 左半[::-1]。
# 去重技巧：排序后，跳过与前一相同且前一未使用的字符。
#
# 时间复杂度: O((n/2)!) — 最坏情况生成所有排列
# 空间复杂度: O(n) — 递归深度和结果存储
#
# 关键点：
# - 先判断可行性再生成
# - 半部分回溯 + 去重
# - 回文构造：left + mid + reverse(left)
