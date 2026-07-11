"""
LeetCode #1573 - Number of Ways to Split a String
中文题名：分割字符串的方案数
https://leetcode.com/problems/number-of-ways-to-split-a-string/


Given a binary string `s` (a string consisting only of '0's and '1's), we
can split `s` into 3 non-empty strings s1, s2, s3 (s1+
s2+ s3 = s).

Return the number of ways `s` can be split such that the number of characters
'1' is the same in s1, s2, and s3.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"

Example 2:

Input: s = "1001"
Output: 0

Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"

Example 4:

Input: s = "100100010100110"
Output: 12

Constraints:

`s[i] == '0'` or `s[i] == '1'`

`3 <= s.length <= 10^5`

【中文翻译】
给定一个二进制字符串 s，将 s 分割成三个非空子字符串 s1、s2、s3（s1+s2+s3=s）。
返回使 s1、s2、s3 中 '1' 的数量相等的分割方案数。答案对 10^9+7 取模。

示例 1：
输入：s = "10101"
输出：4

示例 2：
输入：s = "1001"
输出：0

示例 3：
输入：s = "0000"
输出：3
"""

from typing import List, Optional


class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        total_ones = s.count('1')
        if total_ones % 3 != 0:
            return 0
        n = len(s)
        if total_ones == 0:
            # All zeros: choose 2 split points from n-1 gaps
            return ((n - 1) * (n - 2) // 2) % MOD
        target = total_ones // 3
        count = 0
        first_cut = 0
        second_cut = 0
        for ch in s:
            if ch == '1':
                count += 1
            if count == target:
                first_cut += 1
            elif count == 2 * target:
                second_cut += 1
        return (first_cut * second_cut) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 统计字符串中 '1' 的总数。如果 total_ones % 3 != 0，无解。
# 如果 total_ones == 0，任意选择 2 个分割点都可以，方案数为 C(n-1, 2)。
# 否则，需要将 '1' 分成三等份。第一个分割点可以在第一组 target 个 '1' 之后、
# 第二组第一个 '1' 之前的任意位置（即第一组最后一个 '1' 到第二组第一个 '1' 之间的 0 的数量 +1 种选择）。
# 同理第二个分割点。答案 = first_cut * second_cut % MOD。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 每份必须有恰好 total_ones/3 个 1
# - 第一个分割点在第一份 target 个 1 之后的 0 中
# - 全 0 情况用组合数












