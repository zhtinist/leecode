"""
LeetCode #1641 - Count Sorted Vowel Strings
中文题名：统计字典序元音字符串的数目
https://leetcode.com/problems/count-sorted-vowel-strings/

Given an integer `n`, return the number of strings of
length `n` that consist only of vowels
(`a`, `e`, `i`, `o`, `u`)
and are lexicographically sorted.

A string `s` is lexicographically sorted if for all valid
`i`, `s[i]` is the same as or comes before `s[i+1]`
in the alphabet.

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are `["a","e","i","o","u"].`

Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:

Input: n = 33
Output: 66045

Constraints:

`1 <= n <= 50`

【中文翻译】
给定一个整数 n，返回长度为 n 的、仅由元音字母 (a, e, i, o, u) 组成且按字典序排列的字符串数量。
字符串 s 按字典序排列意味着对于所有有效的 i，s[i] 在字母表中不比 s[i+1] 靠后。

示例 1：
输入: n = 1
输出: 5
解释: 5 个排序字符串为 ["a","e","i","o","u"]。

示例 2：
输入: n = 2
输出: 15
解释: 15 个排序字符串为 ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]。
"""

from typing import List, Optional


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5

        for i in range(2, n + 1):
            for j in range(1, 5):
                dp[j] += dp[j - 1]

        return sum(dp)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。dp[j] 表示以第 j 个元音字母结尾的长度为 i 的字符串数量。
# dp_new[j] = sum(dp[k]) for k <= j（因为字典序要求后面的字母不能小于前面的）。
# 初始 dp = [1,1,1,1,1]（长度为 1）。也可用组合数学：C(n+4, 4)。
#
# 时间复杂度: O(N) — 每次迭代 O(5) = O(1)
# 空间复杂度: O(1) — 仅使用长度为 5 的数组
#
# 关键点:
# - dp[j] += dp[j-1] 是经过化简的前缀和更新
# - 最终答案为 sum(dp)，即所有以不同元音结尾的字符串总数
