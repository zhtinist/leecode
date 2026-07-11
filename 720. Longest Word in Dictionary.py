"""
LeetCode #720 - Longest Word in Dictionary
中文题名：词典中最长的单词
https://leetcode.com/problems/longest-word-in-dictionary/

Given a list of strings `words` representing an English Dictionary, find the
longest word in `words` that can be built one character at a time by other words
in `words`. If there is more than one possible answer, return the longest word
with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:

All the strings in the input will only contain lowercase letters.

The length of `words` will be in the range `[1, 1000]`.

The length of `words[i]` will be in the range `[1, 30]`.

【中文翻译】
给出一个字符串数组 words 组成的一本英语词典。从中找出最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。

示例 1：

输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释：
单词 "world" 可由 "w", "wo", "wor", 和 "worl" 逐步添加一个字母组成。

示例 2：

输入：
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释：
"apply" 和 "apple" 都能由词典中的其他单词组成。但是 "apple" 的字典序小于 "apply"。

注意：

所有输入的字符串都只包含小写字母。

words 数组长度范围为 [1, 1000]。

words[i] 的长度范围为 [1, 30]。
"""

from typing import List, Optional


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        word_set = set([""])
        result = ""
        for word in words:
            if word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(result):
                    result = word
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先对 words 进行排序（按字典序），这样在长度相同时字典序小的会先处理。
# 使用一个集合 word_set 记录所有可以通过逐步添加一个字母构建的单词，初始放入空字符串 ""。
# 遍历排序后的每个单词：检查其去掉最后一个字符的前缀 word[:-1] 是否在集合中。
# 如果在，说明该单词可以被构建，将其加入集合，并更新最长结果。
#
# 时间复杂度: O(N * L * log N) - N 为单词数，L 为单词长度，排序 O(N log N * L)，遍历 O(N * L)
# 空间复杂度: O(N * L) - 集合存储所有构建单词
#
# 关键点:
# - 排序确保字典序小的优先被处理，长度相同时自动保留字典序最小的
# - 空字符串 "" 作为初始种子，使得单字母单词可以被构建
# - 每个单词只需检查去掉最后一个字符的前缀是否已存在于集合中
