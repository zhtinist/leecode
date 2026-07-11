"""
LeetCode #3121 - Count the Number of Special Characters II
统计特殊字母的数量 II
https://leetcode.cn/problems/count-the-number-of-special-characters-ii/

给你一个字符串 `word`。如果 `word` 中同时出现某个字母 `c` 的小写形式和大写形式，并且 每个 小写形式的 `c` 都出现在第一个大写形式的 `c` 之前，则称字母 `c` 是一个 特殊字母 。
返回 `word` 中 特殊字母 的数量。

示例 1:

输入：word = "aaAbcBC"
输出：3
解释：
特殊字母是 `'a'`、`'b'` 和 `'c'`。
示例 2:

输入：word = "abc"
输出：0
解释：
`word` 中不存在特殊字母。
示例 3:

输入：word = "AbBCab"
输出：0
解释：
`word` 中不存在特殊字母。

提示：
`1 <= word.length <= 2 * 10^5`
`word` 仅由小写和大写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}   # 每个字母（小写）最后一次出现的下标
        first_upper = {}  # 每个字母（小写）对应大写第一次出现的下标

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                low = ch.lower()
                if low not in first_upper:
                    first_upper[low] = i

        ans = 0
        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                ans += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String
#
# 解题思路:
# 遍历字符串，记录每个字母（统一用小写标识）的最后一次小写出现位置和第一次大写出现位置。
# 对于每个字母，如果同时存在小写和大写，且最后一个小写出现在第一个大写之前，
# 则该字母为特殊字母。统计满足条件的字母数量。
#
# 时间复杂度: O(n)
# 空间复杂度: O(26) = O(1)
#
# 关键点:
# - 小写字母取最后一次出现（确保所有小写在大写前）
# - 大写字母取第一次出现（只需确保第一个大写在所有小写之后）
# - 字母统一用小写作为key映射
