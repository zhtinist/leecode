"""
LeetCode #3084 - Count Substrings Starting and Ending with Given Character
统计以给定字符开头和结尾的子字符串总数
https://leetcode.cn/problems/count-substrings-starting-and-ending-with-given-character/

给你一个字符串 `s` 和一个字符 `c `。返回在字符串 `s` 中并且以 `c` 字符开头和结尾的非空子字符串的总数。

示例 1：

输入：s = "abada", c = "a"
输出：6
解释：以 `"a"` 开头和结尾的子字符串有： `"abada"`、`"abada"`、`"abada"`、`"abada"`、`"abada"`、`"abada"`。
示例 2：

输入：s = "zzz", c = "z"
输出：6
解释：字符串 `s` 中总共有 `6` 个子字符串，并且它们都以 `"z"` 开头和结尾。

提示：
`1 <= s.length <= 10^5`
`s` 和 `c` 均由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        """
        A substring starts and ends with c iff both endpoints are occurrences of c.
        Count occurrences of c: cnt. Number of such substrings = cnt * (cnt + 1) // 2.
        (C(cnt, 2) for length >= 2 + cnt for length 1).
        """
        cnt = s.count(c)
        return cnt * (cnt + 1) // 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, String, Counting
#
# 解题思路:
# 以 c 开头和结尾的子字符串，其首尾两个位置都必须是 c。
# 设 c 在字符串中出现了 cnt 次。任意两个出现位置（可相同）之间的子串都满足条件。
# 包括长度为 1 的子串（起止位置相同）。总数 = C(cnt, 2) + cnt = cnt * (cnt + 1) / 2。
#
# 时间复杂度: O(n)，统计字符出现次数
# 空间复杂度: O(1)
#
# 关键点:
# - 子串只需首尾是 c，中间可以是任意字符
# - 任意两个 c 的位置对（包括相同位置）唯一确定一个满足条件的子串
# - 公式 cnt*(cnt+1)/2 可直接计算
