"""
LeetCode #692 - Top K Frequent Words
中文题名：前K个高频单词
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same
frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

You may assume k is always valid, 1 <= k <= number of unique elements.

Input words contain only lowercase letters.

Follow up:

Try to solve it in O(n log k) time and O(n) extra
space.

【中文翻译】
给定一个非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应按频率从高到低排序。如果两个单词的频率相同，则按字母顺序较小的在前。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解释: "i" 和 "love" 是出现次数最多的两个单词。
注意，"i" 因字母顺序较小而排在 "love" 之前。

示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解释: "the"、"is"、"sunny" 和 "day" 是出现次数最多的四个单词，出现次数分别为 4、3、2 和 1。

注意：

你可以假设 k 总是有效的，1 <= k <= 不同元素的数量。

输入的单词只包含小写字母。

进阶：

尝试在 O(n log k) 时间和 O(n) 额外空间内解决。
"""

from typing import List, Optional


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        freq = Counter(words)
        sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
        return sorted_words[:k]









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 使用 Counter 统计每个单词的频率 O(n)。
# 2. 对单词按 (-frequency, word) 排序：频率高的在前，频率相同时字典序小的在前。
# 3. 取前 k 个即可。
# 进阶 O(n log k) 方案：使用最小堆，维护大小为 k，按 (frequency, -word_lexicographical) 排序。
#
# 时间复杂度: O(n log n) - 排序；使用堆可以达到 O(n log k)
# 空间复杂度: O(n) - Counter 存储频率
#
# 关键点:
# - 排序 key 为 (-频率, 单词) 同时满足两个排序条件
# - 频率降序（负号），字母升序（默认）
