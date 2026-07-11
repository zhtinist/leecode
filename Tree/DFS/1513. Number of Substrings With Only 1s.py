"""
LeetCode #1513 - Number of Substrings With Only 1s
中文题名：仅含 1 的子串数
https://leetcode.com/problems/number-of-substrings-with-only-1s/

Given a binary string `s` (a string consisting only of '0' and
'1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.

Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.

Example 4:

Input: s = "000"
Output: 0

Constraints:

`s[i] == '0'` or `s[i] == '1'`

`1 <= s.length <= 10^5`

【中文翻译】
给定一个二进制字符串 s（只包含 '0' 和 '1'）。
返回所有字符都为 1 的子字符串的数量。答案可能很大，返回对 10^9+7 取模的结果。

示例 1：

输入：s = "0110111"
输出：9
解释：共有 9 个子字符串只包含 1。"1" 出现 5 次，"11" 出现 3 次，"111" 出现 1 次。

示例 2：

输入：s = "101"
输出：2

示例 3：

输入：s = "111111"
输出：21

示例 4：

输入：s = "000"
输出：0
"""

from typing import List, Optional


class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        result = 0
        count = 0  # consecutive ones
        for ch in s:
            if ch == '1':
                count += 1
                result = (result + count) % MOD
            else:
                count = 0
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 遍历字符串，统计连续的 '1' 的个数 count。
# 每当遇到一个 '1'，以该位置结尾的、全为 1 的子串数量恰好为 count。
# 例如 "111"：第一个 1 贡献 1，第二个 1 贡献 2（"1","11"），第三个 1 贡献 3。
# 遇到 '0' 时将 count 重置为 0。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 连续 k 个 1 贡献 k*(k+1)/2 个子串，可以在遍历中累加
# - 以当前字符结尾的全 1 子串数量 = 连续 1 的长度
# - 注意取模
