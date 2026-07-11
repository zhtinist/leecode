"""
LeetCode #1297 - Maximum Number of Occurrences of a Substring
中文题名：子串的最大出现次数
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

Given a string `s`, return the maximum number of ocurrences of any
substring under the following rules:

The number of unique characters in the substring must be less than or equal to
`maxLetters`.

The substring size must be between `minSize` and `maxSize` inclusive.

Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

Example 3:

Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3

Example 4:

Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0

Constraints:

`1 <= s.length <= 10^5`

`1 <= maxLetters <= 26`

`1 <= minSize <= maxSize <= min(26, s.length)`

`s` only contains lowercase English letters.

【中文翻译】
给定一个字符串 s，根据以下规则，返回任意子串的最大出现次数：

子串中唯一字符的个数必须小于或等于 maxLetters。
子串的长度必须在 minSize 到 maxSize 之间（包含两端）。

示例 1：

输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足条件：2 个唯一字母和长度为 3（在 minSize 和 maxSize 之间）。

示例 2：

输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在字符串中出现了 2 次。它可以重叠。

示例 3：

输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3

示例 4：

输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0

约束条件：

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict

        freq_map = defaultdict(int)
        result = 0

        # Key insight: only need to check substrings of length minSize.
        # A longer substring contains a minSize prefix; if the longer one
        # satisfies maxLetters, so does its minSize prefix.
        # And the prefix appears at least as many times as the longer substring.

        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            # Count unique characters in this substring
            unique_chars = len(set(sub))
            if unique_chars <= maxLetters:
                freq_map[sub] += 1
                result = max(result, freq_map[sub])

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键洞察：只需要检查长度为 minSize 的子串。
# 原因：如果一个更长的子串（长度在 [minSize, maxSize] 之间）满足 maxLetters 条件，
# 那么它的长度为 minSize 的前缀也一定满足（因为前缀的唯一字符数不会超过整个子串）。
# 而且前缀的出现次数不会少于更长子串的出现次数。
# 因此最大值一定在长度为 minSize 的子串中产生。
#
# 算法：
# 1. 遍历所有长度为 minSize 的子串。
# 2. 对每个子串统计其中唯一字符的个数。
# 3. 若唯一字符数 <= maxLetters，则将该子串的出现次数 +1。
# 4. 维护最大出现次数。
#
# 时间复杂度: O(n * minSize) - 遍历 n-minSize+1 个子串，每个检查 minSize 个字符
#   由于 minSize <= 26，实际上还是 O(n)
# 空间复杂度: O(n) - 哈希表存储所有可能子串的频率
#
# 关键点:
# - 只需考虑长度为 minSize 的子串，因为更长的子串不会带来更高的出现次数
# - 使用集合统计每种子串的唯一字符数
# - 子串可以重叠，每种不同子串作为一个整体统计
