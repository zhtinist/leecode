"""
LeetCode #1653 - Minimum Deletions to Make String Balanced
中文题名：使字符串平衡的最少删除次数
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

You are given a string `s` consisting only of characters `'a'`
and `'b'`​​​​.

You can delete any number of characters in `s` to make `s`
balanced. `s` is balanced if there is
no pair of indices `(i,j)` such that `i < j` and `s[i]
= 'b'` and `s[j]= 'a'`.

Return the minimum number of deletions needed to make
`s` balanced.

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

Constraints:

`1 <= s.length <= 105`

`s[i]` is `'a'` or `'b'`​​.

【中文翻译】
给定只包含字符 'a' 和 'b' 的字符串 s。每次操作可删除任意位置的一个字符。
求使字符串成为平衡的最少操作次数。平衡字符串定义为所有 'a' 都在所有 'b' 之前。

示例 1：
输入: s = "aababbab"
输出: 2
解释: 删除 s[2] 的 'b' (变成 "aaabbab") 和 s[6] 的 'a' (变成 "aaabbb")。
"""

from typing import List, Optional


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a_right = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            count_a_right[i] = count_a_right[i + 1] + (1 if s[i] == 'a' else 0)

        count_b_left = 0
        ans = float('inf')
        for i in range(n + 1):
            deletions = count_b_left + count_a_right[i]
            ans = min(ans, deletions)
            if i < n and s[i] == 'b':
                count_b_left += 1

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 最终平衡状态：前面全是 'a'，后面全是 'b'。枚举分界点 i（0 到 n）：
# - s[0..i-1] 应该全是 'a'，需要删除其中的所有 'b'（count_b_left）
# - s[i..n-1] 应该全是 'b'，需要删除其中的所有 'a'（count_a_right[i]）
# 最小删除次数 = min(count_b_left + count_a_right[i]) for all i。
#
# 时间复杂度: O(N) — 预处理后缀和 + 一次遍历
# 空间复杂度: O(N) — 后缀数组
#
# 关键点:
# - 最终状态是全 a 后全 b，分界点可在这之间的任意位置
# - 等价于删除所有参与 ba 模式的字符
