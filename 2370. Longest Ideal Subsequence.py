"""
LeetCode #2370 - Longest Ideal Subsequence
最长理想子序列
https://leetcode.cn/problems/longest-ideal-subsequence/

给你一个由小写字母组成的字符串 `s` ，和一个整数 `k` 。如果满足下述条件，则可以将字符串 `t` 视作是 理想字符串 ：
`t` 是字符串 `s` 的一个子序列。
`t` 中每两个 相邻 字母在字母表中位次的绝对差值小于或等于 `k` 。
返回 最长 理想字符串的长度。
字符串的子序列同样是一个字符串，并且子序列还满足：可以经由其他字符串删除某些字符（也可以不删除）但不改变剩余字符的顺序得到。
注意：字母表顺序不会循环。例如，`'a'` 和 `'z'` 在字母表中位次的绝对差值是 `25` ，而不是 `1` 。

示例 1：
输入：s = "acfgbd", k = 2 输出：4 解释：最长理想字符串是 "acbd" 。该字符串长度为 4 ，所以返回 4 。 注意 "acfgbd" 不是理想字符串，因为 'c' 和 'f' 的字母表位次差值为 3 。
示例 2：
输入：s = "abcd", k = 3 输出：4 解释：最长理想字符串是 "abcd" ，该字符串长度为 4 ，所以返回 4 。

提示：
`1 <= s.length <= 10^5`
`0 <= k <= 25`
`s` 由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # dp[c] 表示以字母 c 结尾的最长理想子序列的长度
        dp = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            # 在 [idx-k, idx+k] 范围内找最优前驱
            left = max(0, idx - k)
            right = min(25, idx + k)
            best = max(dp[left:right + 1]) + 1
            dp[idx] = best

        return max(dp)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Dynamic Programming
#
# 解题思路:
# 使用动态规划，dp[c] 表示以字母 c（c 从 0 到 25）结尾的最长理想子序列的长度。
# 遍历字符串 s 中的每个字符，对于当前字符对应的索引 idx：
# 在 [idx-k, idx+k] 范围内找到最大的 dp 值作为前驱，
# 然后更新 dp[idx] = best + 1。
# 最终返回 dp 数组中的最大值。
# 因为只关心相邻字符的差值不超过 k，不关心字符在原始字符串中的具体位置，
# 所以用 26 个字母的 dp 数组即可。
#
# 时间复杂度: O(n * k) 其中 n 为字符串长度，k 最大为 25，所以实际上是 O(n)
# 空间复杂度: O(1) dp 数组固定大小为 26
#
# 关键点:
# - dp 数组只需要 26 个位置，每个位置记录以对应字母结尾的最长长度
# - 每次在当前字母的前后 k 范围内找最大 dp 值作为前驱
# - 注意边界处理：left = max(0, idx-k)，right = min(25, idx+k)
