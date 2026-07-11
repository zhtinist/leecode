"""
LeetCode #2063 - Vowels of All Substrings
所有子字符串中的元音
https://leetcode.cn/problems/vowels-of-all-substrings/

给你一个字符串 `word` ，返回 `word` 的所有子字符串中 元音的总数 ，元音是指 `'a'`、`'e'`、`'i'`、`'o'` 和 `'u'` 。
子字符串 是字符串中一个连续（非空）的字符序列。
注意：由于对 `word` 长度的限制比较宽松，答案可能超过有符号 32 位整数的范围。计算时需当心。

示例 1：
输入：word = "aba" 输出：6 解释： 所有子字符串是："a"、"ab"、"aba"、"b"、"ba" 和 "a" 。 - "b" 中有 0 个元音 - "a"、"ab"、"ba" 和 "a" 每个都有 1 个元音 - "aba" 中有 2 个元音 因此，元音总数 = 0 + 1 + 1 + 1 + 1 + 2 = 6 。
示例 2：
输入：word = "abc" 输出：3 解释： 所有子字符串是："a"、"ab"、"abc"、"b"、"bc" 和 "c" 。 - "a"、"ab" 和 "abc" 每个都有 1 个元音 - "b"、"bc" 和 "c" 每个都有 0 个元音 因此，元音总数 = 1 + 1 + 1 + 0 + 0 + 0 = 3 。
示例 3：
输入：word = "ltcd" 输出：0 解释："ltcd" 的子字符串均不含元音。
示例 4：
输入：word = "noosabasboosa" 输出：237 解释：所有子字符串中共有 237 个元音。

提示：
`1 <= word.length <= 10^5`
`word` 由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        total = 0
        for i, ch in enumerate(word):
            if ch in vowels:
                # This vowel appears in (i + 1) substrings ending at or after i
                # and (n - i) substrings starting at or before i
                total += (i + 1) * (n - i)
        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, String, Dynamic Programming, Combinatorics
#
# 解题思路:
# 对于位置i的元音字母，统计它出现在多少个子字符串中。
# 包含位置i的子串 = 左边界可以在[0,i]中选择，右边界可以在[i,n-1]中选择，
# 所以贡献 = (i+1) * (n-i)。遍历字符串，对每个元音累加其贡献即可。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 组合数学：每个位置贡献 = (左边选择数) * (右边选择数)
# - 左边选择数 = i + 1
# - 右边选择数 = n - i
