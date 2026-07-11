"""
LeetCode #2730 - Find the Longest Semi-Repetitive Substring
找到最长的半重复子字符串
https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/

给你一个下标从 0 开始的字符串 `s` ，这个字符串只包含 `0` 到 `9` 的数字字符。
如果一个字符串 `t` 中至多有一对相邻字符是相等的，那么称这个字符串 `t` 是 半重复的 。例如，`"0010"` 、`"002020"` 、`"0123"` 、`"2002"` 和 `"54944"` 是半重复字符串，而 `"00101022"` （相邻的相同数字对是 00 和 22）和 `"1101234883"` （相邻的相同数字对是 11 和 88）不是半重复字符串。
请你返回 `s` 中最长 半重复 子字符串 的长度。

示例 1：

输入：s = "52233"
输出：4
解释：
最长的半重复子字符串是 "5223"。整个字符串 "52233" 有两个相邻的相同数字对 22 和 33，但最多只能选取一个。
示例 2：

输入：s = "5494"
输出：4
解释：
`s` 是一个半重复字符串。
示例 3：

输入：s = "1111111"
输出：2
解释：
最长的半重复子字符串是 "11"。子字符串 "111" 有两个相邻的相同数字对，但最多允许选取一个。

提示：
`1 <= s.length <= 50`
`'0' <= s[i] <= '9'`
"""

from typing import List, Optional


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        pairs = 0
        ans = 0
        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                pairs += 1
            while pairs > 1:
                left += 1
                if s[left] == s[left - 1]:
                    pairs -= 1
            ans = max(ans, right - left + 1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Sliding Window
#
# 解题思路:
# 滑动窗口维护最多包含一对相邻相同字符的子串。右指针扩展时检测新增的相邻相同对。
# 当相邻相同对超过 1 时，收缩左指针直到条件满足。记录过程中最大的窗口长度。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 滑动窗口维护"相邻相同对"的数量，目标是不超过 1 对
# - 收缩时注意检查左指针移出是否消除了一对相邻相同字符
# - 边界条件：单个字符的相邻相同对为 0，始终满足条件
