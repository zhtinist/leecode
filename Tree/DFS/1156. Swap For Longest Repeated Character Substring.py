"""
LeetCode #1156 - Swap For Longest Repeated Character Substring
中文题名：单字符重复子串的最大长度
https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

Given a string `text`, we are allowed to swap two of the characters in the string.
Find the length of the longest substring with repeated characters.

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.

Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.

Example 3:

Input: text = "aaabbaaa"
Output: 4

Example 4:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.

Example 5:

Input: text = "abcdef"
Output: 1

Constraints:

`1 <= text.length <= 20000`

`text` consist of lowercase English characters only.

【中文翻译】
给定一个字符串 text，我们可以交换其中两个字符的位置。求交换后可以得到的最长单字符重复子串的长度。

示例 1：

输入：text = "ababa"
输出：3
解释：我们可以将第一个 'b' 与最后一个 'a' 交换，或将最后一个 'b' 与第一个 'a' 交换。然后，最长的重复字符子串是 "aaa"，长度为 3。

示例 2：

输入：text = "aaabaaa"
输出：6
解释：将 'b' 与最后一个 'a'（或第一个 'a'）交换，我们得到最长的重复字符子串 "aaaaaa"，长度为 6。

示例 3：

输入：text = "aaabbaaa"
输出：4

示例 4：

输入：text = "aaaaa"
输出：5
解释：无需交换，最长的重复字符子串是 "aaaaa"，长度为 5。

示例 5：

输入：text = "abcdef"
输出：1

约束条件：

`1 <= text.length <= 20000`

text 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import defaultdict

        # Count total occurrences of each character
        total_count = defaultdict(int)
        for ch in text:
            total_count[ch] += 1

        n = len(text)
        # Group consecutive identical characters: (char, length)
        groups = []
        i = 0
        while i < n:
            ch = text[i]
            j = i
            while j < n and text[j] == ch:
                j += 1
            groups.append((ch, j - i))
            i = j

        ans = 0
        # Case 1: Within a single group, we can potentially add one more
        # from outside if there's an extra character available
        for ch, length in groups:
            ans = max(ans, min(length + 1, total_count[ch]))

        # Case 2: Two groups of the same character separated by exactly one different character
        for i in range(1, len(groups) - 1):
            if groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1:
                ch = groups[i - 1][0]
                combined = groups[i - 1][1] + groups[i + 1][1]
                # If there's an extra character of this type outside, we can add it
                if total_count[ch] > combined:
                    ans = max(ans, combined + 1)
                else:
                    ans = max(ans, combined)

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先将字符串压缩为连续相同字符的分组列表，每组记录字符和长度。
# 例如 "aaabaaa" -> [('a',3), ('b',1), ('a',3)]
#
# 然后分两种情况考虑：
# 情况一：单个分组。对于某个字符 c 的长度为 len 的连续段，我们可以从字符串中
# 其他地方拿来一个 c 并交换到该段旁边，使长度变为 len + 1。
# 但前提是其他地方确实有一个 c 可用。因此贡献为 min(len + 1, total_count[c])。
#
# 情况二：两个相同字符的连续段之间只隔了一个不同的字符（且该字符长度为 1）。
# 可以将中间那个字符与另一个相同字符交换，将两段连起来。
# 合并后的长度为 left_len + right_len。如果字符总数还有多余的，
# 还可以从其他地方再换一个过来（+1）。
#
# 取所有情况的最大值即为答案。
#
# 时间复杂度: O(n) - 遍历字符串两次（统计 + 分组）
# 空间复杂度: O(k) - k 为连续段数量，最坏 O(n)
#
# 关键点:
# - 将字符串压缩为连续段是核心技巧，简化了分析
# - 情况二要求中间的"间隔字符"长度恰好为 1 才能合并
# - 注意边界：合并后长度不能超过该字符的总数
# - 如果字符总数大于合并后的长度，说明还有额外的相同字符可以交换过来
