"""
LeetCode #244 - Shortest Word Distance II
中文题名：最短单词距离 II
https://leetcode.com/problems/shortest-word-distance-ii/

Design a class which receives a list of words in the constructor, and implements a method
that takes two words *word1* and *word2* and return the shortest distance
between these two words in the list. Your method will be called *repeatedly* many
times with different parameters.

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
设计一个类，在构造函数中接收一个单词列表，并实现一个方法，该方法接收两个单词 *word1* 和 *word2*，并返回列表中这两个单词之间的最短距离。你的方法将被*反复*调用，参数不同。

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


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # 预处理：记录每个单词出现的所有索引
        self.word_indices = {}
        for i, word in enumerate(wordsDict):
            if word not in self.word_indices:
                self.word_indices[word] = []
            self.word_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # 获取两个单词的索引列表（均已排序）
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]

        # 双指针合并两个有序列表，找最小差值
        i = j = 0
        min_dist = float('inf')
        while i < len(indices1) and j < len(indices2):
            min_dist = min(min_dist, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1

        return min_dist


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 构造函数预处理：用哈希表记录每个单词出现的所有索引（自动有序）。
# 查询时用双指针法，在两个有序索引列表上移动，每次将指向较小值的指针
# 前移，同时更新最小距离。类似合并两个有序数组的过程。
#
# 时间复杂度: 构造 O(n)，查询 O(k1 + k2) — k1, k2 为两个单词出现次数
# 空间复杂度: O(n) — 存储所有单词的索引列表
#
# 关键点：
# - 预处理以支持多次查询
# - 双指针在有序列表中高效查找最小差值
# - 避免 O(k1 * k2) 的暴力比较
