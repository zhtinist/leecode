"""
LeetCode #2982 - Find Longest Special Substring That Occurs Thrice II
找出出现至少三次的最长特殊子字符串 II
https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/

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
`3 <= s.length <= 5 * 10^5`
`s` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def maximumLength(self, s: str) -> int:
        """
        For each character, collect run lengths. The top 3 longest runs
        determine the answer: max(a-2, min(a-1, b), c).
        a >= b >= c are the top 3 run lengths (0 if fewer than 3 runs).
        """
        n = len(s)
        # For each of 26 letters, store top 3 run lengths
        top3 = [[0, 0, 0] for _ in range(26)]

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            idx = ord(s[i]) - ord('a')

            # Maintain top 3
            arr = top3[idx]
            if length > arr[0]:
                arr[2] = arr[1]
                arr[1] = arr[0]
                arr[0] = length
            elif length > arr[1]:
                arr[2] = arr[1]
                arr[1] = length
            elif length > arr[2]:
                arr[2] = length

            i = j

        ans = -1
        for a, b, c in top3:
            if a == 0:
                continue
            # Case 1: three from the longest run
            if a >= 3:
                ans = max(ans, a - 2)
            # Case 2: two from longest + one from second longest
            if a >= 2 and b >= 1:
                ans = max(ans, min(a - 1, b))
            # Case 3: one from each of top 3
            if c >= 1:
                ans = max(ans, c)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Binary Search, Counting, Sliding Window
#
# 解题思路:
# 对于每个字符，先扫描字符串找出所有由该字符组成的连续段长度。
# 保留每个字符最长的 3 个连续段长度 a >= b >= c。
# 答案为 max(a-2, min(a-1, b), c)：
# - a-2: 三段都来自最长段（需要 a >= 3）
# - min(a-1, b): 两段来自最长段，一段来自次长段
# - c: 三段各来自一个不同的连续段
#
# 时间复杂度: O(n)，一次遍历扫描所有连续段
# 空间复杂度: O(1)，仅存储 26 个字符的 top3 长度
#
# 关键点:
# - 特殊子串只能由单一字符组成，不同字符之间独立计算
# - 对于长度为 L 的连续段，长度 x 的子串出现 L-x+1 次
# - 只需保留每个字符最长的 3 个段，公式直接给出答案
