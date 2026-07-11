"""
LeetCode #243 - Shortest Word Distance
中文题名：最短单词距离
https://leetcode.com/problems/shortest-word-distance/

Given a list of words and two words *word1* and *word2*, return the shortest
distance between these two words in the list.

Example:

Assume that words = `["practice", "makes", "perfect",
"coding", "makes"]`.

Input: *word1* = `"coding"`, *word2* = `"practice"`
Output: 3

Input: *word1* = `"makes"`, *word2* = `"coding"`
Output: 1

Note:

You may assume that *word1* does not equal to *word2*, and
*word1* and *word2* are both in the list.

【中文翻译】
给定一个单词列表和两个单词 *word1* 和 *word2*，返回列表中这两个单词之间的最短距离。

示例：

假设 words = `["practice", "makes", "perfect", "coding", "makes"]`。

输入：*word1* = `"coding"`，*word2* = `"practice"`
输出：3

输入：*word1* = `"makes"`，*word2* = `"coding"`
输出：1

注意：

你可以假设 *word1* 不等于 *word2*，且 *word1* 和 *word2* 都在列表中。
"""

from typing import List, Optional


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # 记录最近一次出现的位置
        idx1 = -1
        idx2 = -1
        min_dist = float('inf')

        for i, word in enumerate(wordsDict):
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
# Difficulty: Easy
# Paid Only: Yes
#
# 解题思路：
# 一次遍历数组，维护 word1 和 word2 最近一次出现的索引。每遇到其中一个词，
# 如果另一个词的索引已经记录过，就计算距离并更新最小值。
#
# 时间复杂度: O(n) — 遍历数组一次
# 空间复杂度: O(1) — 只使用常数个变量
#
# 关键点：
# - 不需要存储所有位置，只需记录最近出现的索引
# - 遇到任一单词时检查另一个是否已出现，即时更新最小距离
