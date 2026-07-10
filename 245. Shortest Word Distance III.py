"""
LeetCode #245 - Shortest Word Distance III
https://leetcode.com/problems/shortest-word-distance-iii/

Given a list of words and two words *word1* and *word2*, return the shortest
distance between these two words in the list.

*word1* and *word2* may be the same and they represent two individual words in
the list.

Example:

Assume that words = `["practice", "makes", "perfect",
"coding", "makes"]`.

Input: *word1* = `"makes"`, *word2* = `"coding"`
Output: 1

Input: *word1* = `"makes"`, *word2* = `"makes"`
Output: 3

Note:

You may assume *word1* and *word2* are both in the list.
"""

from typing import List, Optional


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = idx2 = -1
        min_dist = float('inf')
        same_word = (word1 == word2)
        # prev 用于当 word1 == word2 时记录上一个位置
        prev = -1

        for i, word in enumerate(wordsDict):
            if same_word:
                if word == word1:
                    if prev != -1:
                        min_dist = min(min_dist, i - prev)
                    prev = i
            else:
                if word == word1:
                    idx1 = i
                    if idx2 != -1:
                        min_dist = min(min_dist, abs(idx1 - idx2))
                elif word == word2:
                    idx2 = i
                    if idx1 != -1:
                        min_dist = min(min_dist, abs(idx2 - idx1))

        return min_dist


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 与 #243 类似，但需要处理 word1 == word2 的特殊情况。如果两个单词相同，
# 只需记录该单词上一次出现的位置 prev，每次再遇到时计算与 prev 的距离
# 并更新最小值。如果不同，与 #243 逻辑完全相同。
#
# 时间复杂度: O(n) — 遍历数组一次
# 空间复杂度: O(1) — 常数个变量
#
# 关键点：
# - 区分 word1 == word2 的情况
# - 相同时：记录上一个位置 prev，每次遇到计算 i - prev
# - 不同时：与 #243 相同逻辑
