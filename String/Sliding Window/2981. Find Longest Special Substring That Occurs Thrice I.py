"""
LeetCode #2981 - Find Longest Special Substring That Occurs Thrice I
找出出现至少三次的最长特殊子字符串 I
https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-i/

给你一个仅由小写英文字母组成的字符串 `s` 。
如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 `"abc"` 不是特殊字符串，而字符串 `"ddd"`、`"zz"` 和 `"f"` 是特殊字符串。
返回在 `s` 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 `-1` 。
子字符串 是字符串中的一个连续 非空 字符序列。

示例 1：
输入：s = "aaaa" 输出：2 解释：出现三次的最长特殊子字符串是 "aa" ：子字符串 "aaaa"、"aaaa" 和 "aaaa"。 可以证明最大长度是 2 。
示例 2：
输入：s = "abcdef" 输出：-1 解释：不存在出现至少三次的特殊子字符串。因此返回 -1 。
示例 3：
输入：s = "abcaba" 输出：1 解释：出现三次的最长特殊子字符串是 "a" ：子字符串 "abcaba"、"abcaba" 和 "abcaba"。 可以证明最大长度是 1 。

提示：
`3 <= s.length <= 50`
`s` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def maximumLength(self, s: str) -> int:
        """
        Since n <= 50, brute force: enumerate all special substrings
        (single-character runs) and count their occurrences.
        """
        from collections import Counter

        n = len(s)
        cnt = Counter()

        for i in range(n):
            for j in range(i, n):
                if s[j] != s[i]:
                    break
                cnt[s[i:j + 1]] += 1

        ans = -1
        for sub, count in cnt.items():
            if count >= 3:
                ans = max(ans, len(sub))

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Binary Search, Counting, Sliding Window
#
# 解题思路:
# n <= 50，直接暴力枚举所有特殊子字符串（由单一字符组成的连续子串）。
# 对于每个起始位置 i，向右扩展直到字符变化，将每个子串加入计数器。
# 最后找出计数 >= 3 的最长子串长度。
#
# 时间复杂度: O(n^2)，n <= 50，完全可行
# 空间复杂度: O(n^2)，存储所有特殊子串
#
# 关键点:
# - 特殊子串由单一字符组成，只需考虑由相同字符构成的连续段
# - 暴力枚举所有可能的起止位置即可
# - 小数据范围使得简单方法直接通过
