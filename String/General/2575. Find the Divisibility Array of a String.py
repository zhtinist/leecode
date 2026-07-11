"""
LeetCode #2575 - Find the Divisibility Array of a String
找出字符串的可整除数组
https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/

给你一个下标从 0 开始的字符串 `word` ，长度为 `n` ，由从 `0` 到 `9` 的数字组成。另给你一个正整数 `m` 。
`word` 的 可整除数组 `div`  是一个长度为 `n` 的整数数组，并满足：
如果 `word[0,...,i]` 所表示的 数值 能被 `m` 整除，`div[i] = 1`
否则，`div[i] = 0`
返回 `word` 的可整除数组。

示例 1：
输入：word = "998244353", m = 3 输出：[1,1,0,0,0,1,1,0,0] 解释：仅有 4 个前缀可以被 3 整除："9"、"99"、"998244" 和 "9982443" 。
示例 2：
输入：word = "1010", m = 10 输出：[0,1,0,1] 解释：仅有 2 个前缀可以被 10 整除："10" 和 "1010" 。

提示：
`1 <= n <= 10^5`
`word.length == n`
`word` 由数字 `0` 到 `9` 组成
`1 <= m <= 10^9`
"""

from typing import List, Optional


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        rem = 0
        for ch in word:
            rem = (rem * 10 + int(ch)) % m
            ans.append(1 if rem == 0 else 0)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, String
#
# 解题思路:
# 使用模运算的递推性质：前i位数字组成的数num_i = num_{i-1} * 10 + digit_i。
# 对m取模：rem_i = (rem_{i-1} * 10 + digit_i) % m。若当前余数为0则前缀可被m整除。
# 不需要构建大整数，避免溢出和性能问题。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)（不计输出数组）
#
# 关键点:
# - (a * 10 + b) % m = ((a % m) * 10 + b) % m 模运算递推
# - 无需构造完整大整数，边读边取模
# - 结果数组与输入等长
