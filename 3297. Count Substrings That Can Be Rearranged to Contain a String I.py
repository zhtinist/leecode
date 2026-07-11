"""
LeetCode #3297 - Count Substrings That Can Be Rearranged to Contain a String I
统计重新排列后包含另一个字符串的子字符串数目 I
https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

给你两个字符串 `word1` 和 `word2` 。
如果一个字符串 `x` 重新排列后，`word2` 是重排字符串的 前缀 ，那么我们称字符串 `x` 是 合法的 。
请你返回 `word1` 中 合法 子字符串 的数目。

示例 1：

输入：word1 = "bcca", word2 = "abc"
输出：1
解释：
唯一合法的子字符串是 `"bcca"` ，可以重新排列得到 `"abcc"` ，`"abc"` 是它的前缀。
示例 2：

输入：word1 = "abcabc", word2 = "abc"
输出：10
解释：
除了长度为 1 和 2 的所有子字符串都是合法的。
示例 3：

输入：word1 = "abcabc", word2 = "aaabc"
输出：0

解释：
`1 <= word1.length <= 10^5`
`1 <= word2.length <= 10^4`
`word1` 和 `word2` 都只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        from collections import Counter
        need = Counter(word2)
        required = len(need)
        n = len(word1)
        ans = 0
        left = 0
        formed = 0
        window = Counter()

        for right, ch in enumerate(word1):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                # 收缩左边界直到不满足条件
                left_ch = word1[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

            # left 当前指向第一个使窗口不满足条件的位置
            # 所有左边界在 [0, left-1] 的子串 [l, right] 都满足条件
            ans += left

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Sliding Window
#
# 解题思路:
# 重排后 word2 是前缀 → 子串需要包含 word2 的所有字符（且数量足够）。
# 滑动窗口：右指针扩展窗口统计字符频率，当窗口满足条件（包含 word2 所有字符各足够数量），
# 收缩左指针直到刚好不满足条件。对于每个右边界 right，收缩后的 left 指向第一个
# 使窗口不满足条件的位置，因此所有左边界在 [0, left-1] 的子串都满足条件。
# ans += left（对每个 right 累加合法左边界数量）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)（字母表 26 个）
#
# 关键点:
# - "包含所有字符" 的滑动窗口模式
# - formed 计数跟踪已满足的字符种类数
# - ans += left 巧妙统计所有合法子串
#
# 时间复杂度: O(n) — n = len(word1)
# 空间复杂度: O(1) — 字母表大小固定
#
# 关键点:
# - 滑动窗口 + "覆盖所有所需字符" 模式
# - 对每个右边界，计数满足覆盖条件的左边界数量
