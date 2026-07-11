"""
LeetCode #2522 - Partition String Into Substrings With Values at Most K
将字符串分割成值不超过 K 的子字符串
https://leetcode.cn/problems/partition-string-into-substrings-with-values-at-most-k/

给你一个字符串 `s` ，它每一位都是 `1` 到 `9` 之间的数字组成，同时给你一个整数 `k` 。
如果一个字符串 `s` 的分割满足以下条件，我们称它是一个 好 分割：
`s` 中每个数位 恰好 属于一个子字符串。
每个子字符串的值都小于等于 `k` 。
请你返回 `s` 所有的 好 分割中，子字符串的 最少 数目。如果不存在 `s` 的 好 分割，返回 `-1` 。
注意：
一个字符串的 值 是这个字符串对应的整数。比方说，`"123"` 的值为 `123` ，`"1"` 的值是 `1` 。
子字符串 是字符串中一段连续的字符序列。

示例 1：
输入：s = "165462", k = 60 输出：4 解释：我们将字符串分割成子字符串 "16" ，"54" ，"6" 和 "2" 。每个子字符串的值都小于等于 k = 60 。 不存在小于 4 个子字符串的好分割。
示例 2：
输入：s = "238182", k = 5 输出：-1 解释：这个字符串不存在好分割。

提示：
`1 <= s.length <= 10^5`
`s[i]` 是 `'1'` 到 `'9'` 之间的数字。
`1 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur_val = 0
        count = 0
        for ch in s:
            d = int(ch)
            if d > k:
                return -1
            cur_val = cur_val * 10 + d
            if cur_val > k:
                count += 1
                cur_val = d
        return count + 1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String, Dynamic Programming
#
# 解题思路:
# 贪心从左到右扫描：尽可能延长当前子字符串（即追加数字后值仍<=k就追加），
# 若当前数字本身>k则无法分割返回-1。当追加下一个数字会导致超k时，切断并开始新段。
# 这种方法能保证子字符串数量最少。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 单个数字大于k时直接返回-1
# - 贪心延长当前段一定是最优的（因为值不超过k的前提下多取一个不会增加段数）
# - 注意处理cur_val乘法溢出：Python自动处理大整数，但k<=10^9限制了值范围
