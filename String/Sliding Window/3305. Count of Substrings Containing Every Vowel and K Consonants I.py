"""
LeetCode #3305 - Count of Substrings Containing Every Vowel and K Consonants I
元音辅音字符串计数 I
https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

给你一个字符串 `word` 和一个 非负 整数 `k`。
返回 `word` 的 子字符串 中，每个元音字母（`'a'`、`'e'`、`'i'`、`'o'`、`'u'`）至少 出现一次，并且 恰好 包含 `k` 个辅音字母的子字符串的总数。

示例 1：

输入：word = "aeioqq", k = 1
输出：0
解释：
不存在包含所有元音字母的子字符串。
示例 2：

输入：word = "aeiou", k = 0
输出：1
解释：
唯一一个包含所有元音字母且不含辅音字母的子字符串是 `word[0..4]`，即 `"aeiou"`。
示例 3：

输入：word = "ieaouqqieaouqq", k = 1
输出：3
解释：
包含所有元音字母并且恰好含有一个辅音字母的子字符串有：
`word[0..5]`，即 `"ieaouq"`。
`word[6..11]`，即 `"qieaou"`。
`word[7..12]`，即 `"ieaouq"`。

提示：
`5 <= word.length <= 250`
`word` 仅由小写英文字母组成。
`0 <= k <= word.length - 5`
"""

from typing import List, Optional


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(word)
        ans = 0
        # 对于每个左边界，滑动窗口
        for i in range(n):
            vowel_cnt = {}
            consonant_cnt = 0
            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    vowel_cnt[ch] = vowel_cnt.get(ch, 0) + 1
                else:
                    consonant_cnt += 1
                    if consonant_cnt > k:
                        break
                if consonant_cnt == k and len(vowel_cnt) == 5:
                    ans += 1
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Sliding Window
#
# 解题思路:
# n <= 250，O(n^2) 暴力可行。枚举所有子串，统计元音和辅音数量。
# 对每个子串：维护 5 个元音字母的频率和辅音计数。
# 当辅音数 == k 且包含全部 5 种元音时，结果 +1。
# 如果辅音数超过 k 可以提前 break（因为继续扩展只会增加辅音）。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(1)
#
# 关键点:
# - 小数据量允许暴力枚举
# - 辅音超过 k 时剪枝提前退出内层循环
