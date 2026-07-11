"""
LeetCode #424 - Longest Repeating Character Replacement
中文题名：替换后的最长重复字符
https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string `s` that consists of only uppercase English letters, you can
perform at most `k` operations on that string.

In one operation, you can choose any character of the string and change it
to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after
performing the above operations.

Note:

Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

【中文翻译】
给你一个仅由大写英文字母组成的字符串 s，你可以最多执行 k 次操作。

在一次操作中，你可以选择字符串中的任何一个字符，并将其更改为任何其他大写英文字母。

请你找出执行上述操作后，包含重复字母的最长子字符串的长度。

注意：

字符串长度和 k 都不会超过 10^4。

示例 1：

输入：
s = "ABAB", k = 2

输出：
4

解释：
将两个 'A' 替换为两个 'B'，反之亦然。

示例 2：

输入：
s = "AABABBA", k = 1

输出：
4

解释：
将中间的一个 'A' 替换为 'B' 后形成 "AABBBBA"。
子串 "BBBB" 有最长重复字母，长度为 4。
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq = 0
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            window_len = right - left + 1
            if window_len - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口 + 贪心：
# 1. 维护一个窗口 [left, right]，统计窗口内各字符频率。
# 2. max_freq 记录窗口内出现次数最多的字符的频率。
# 3. 窗口内需要替换的字符数 = window_len - max_freq。
# 4. 当 window_len - max_freq > k 时，窗口不合法，收缩左边界。
# 5. 记录每个合法窗口的最大长度。
# 关键优化：max_freq 不需要在收缩时精确减小。
#   因为只有当窗口内某字符的频率超过 max_freq 时，窗口才可能更大。
#   所以 max_freq 只增不减（或说"不收缩时不需要回退"），这不会影响正确性。
#   要理解：不影响最终答案是窗口长度可能偏大，但 max_len 记录的永远是正确的。
#   当 left 右移时，窗口变小，结果不会变得更优。
#
# 时间复杂度: O(n)，每个字符最多被访问两次
# 空间复杂度: O(1)，字母表大小固定为 26
#
# 关键点:
# - 滑动窗口适用条件：可替换字符数 <= k
# - max_freq 维护当前窗口的最高频率字符（不用每次遍历 26 个字母重新计算）
# - win_len - max_freq 是需替换的字符数
# - 窗口只增大不缩小（记录最大长度），左指针只在需要时右移
