"""
LeetCode #2531 - Make Number of Distinct Characters Equal
使字符串中不同字符的数目相等
https://leetcode.cn/problems/make-number-of-distinct-characters-equal/

给你两个下标从 0 开始的字符串 `word1` 和 `word2` 。
一次 移动 由以下两个步骤组成：
选中两个下标 `i` 和 `j` ，分别满足 `0 <= i < word1.length` 和 `0 <= j < word2.length` ，
交换 `word1[i]` 和 `word2[j]` 。
如果可以通过 恰好一次 移动，使 `word1` 和 `word2` 中不同字符的数目相等，则返回 `true` ；否则，返回 `false` 。

示例 1：
输入：word1 = "ac", word2 = "b" 输出：false 解释：交换任何一组下标都会导致第一个字符串中有 2 个不同的字符，而在第二个字符串中只有 1 个不同字符。
示例 2：
输入：word1 = "abcc", word2 = "aab" 输出：true 解释：交换第一个字符串的下标 2 和第二个字符串的下标 0 。之后得到 word1 = "abac" 和 word2 = "cab" ，各有 3 个不同字符。
示例 3：
输入：word1 = "abcde", word2 = "fghij" 输出：true 解释：无论交换哪一组下标，两个字符串中都会有 5 个不同字符。

提示：
`1 <= word1.length, word2.length <= 10^5`
`word1` 和 `word2` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for ch in word1:
            cnt1[ord(ch) - 97] += 1
        for ch in word2:
            cnt2[ord(ch) - 97] += 1

        dist1 = sum(1 for c in cnt1 if c > 0)
        dist2 = sum(1 for c in cnt2 if c > 0)

        for a in range(26):
            if cnt1[a] == 0:
                continue
            for b in range(26):
                if cnt2[b] == 0:
                    continue
                if a == b:
                    if dist1 == dist2:
                        return True
                    continue
                # swap char a from word1 with char b from word2
                new_dist1 = dist1
                if cnt1[a] == 1:
                    new_dist1 -= 1
                if cnt1[b] == 0:
                    new_dist1 += 1

                new_dist2 = dist2
                if cnt2[b] == 1:
                    new_dist2 -= 1
                if cnt2[a] == 0:
                    new_dist2 += 1

                if new_dist1 == new_dist2:
                    return True

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Counting
#
# 解题思路:
# 统计两个单词中每个字符的频率和不同字符数。枚举所有26*26种可能的字符交换组合。
# 对于每种交换(a从word1, b从word2)，模拟交换后两个单词的不同字符数变化：
# 若移除的字符频率为1则dist-1，若新增的字符原来频率为0则dist+1。
# 存在任一组合使dist1==dist2即可返回True。
#
# 时间复杂度: O(N+M+26*26)，N、M为两字符串长度
# 空间复杂度: O(1)，只需26个字符的计数
#
# 关键点:
# - 只需枚举26个字符而非所有下标组合
# - 模拟交换只需检查字符频率的边界变化（1->0和0->1）
# - 同字符交换时dist不变，直接比较原始dist是否相等
