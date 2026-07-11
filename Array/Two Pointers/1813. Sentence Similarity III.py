"""
LeetCode #1813 - Sentence Similarity III
中文题名：句子相似性 III
https://leetcode.com/problems/sentence-similarity-iii/

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, `"Hello World"`, `"HELLO"`, `"hello world hello world"` are all sentences. Words consist of only uppercase and lowercase English letters.

Two sentences `sentence1` and `sentence2` are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, `sentence1 = "Hello my name is Jane"` and `sentence2 = "Hello Jane"` can be made equal by inserting `"my name is"` between `"Hello"` and `"Jane"` in `sentence2`.

Given two sentences `sentence1` and `sentence2`, return `true` if `sentence1` and `sentence2` are similar. Otherwise, return `false`.

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

Example 4:

Input: sentence1 = "Luky", sentence2 = "Lucccky"
Output: false

Constraints:

`1 <= sentence1.length, sentence2.length <= 100`

`sentence1` and `sentence2` consist of lowercase and uppercase English letters and spaces.

The words in `sentence1` and `sentence2` are separated by a single space.

【中文翻译】
给定两个句子 sentence1 和 sentence2，每个句子由空格分隔的单词组成。
一个句子可以通过在一个句子中插入另一个句子（作为连续段）而得到。
判断两个句子是否相似（即是否可以通过插入操作相互转换）。
注意插入的句子必须与另一个句子的前后部分完全匹配。

示例 1：
输入: sentence1 = "My name is Haley", sentence2 = "My Haley"
输出: true
解释: 在 sentence2 中插入 "name is" 得到 sentence1。
相当于 sentence1 的前缀 "My" 和后缀 "Haley" 分别匹配 sentence2。
"""

from typing import List, Optional


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        # 确保 words1 是较长的
        if len(words1) < len(words2):
            words1, words2 = words2, words1

        n1, n2 = len(words1), len(words2)

        # 从左边匹配
        left = 0
        while left < n2 and words1[left] == words2[left]:
            left += 1

        # 从右边匹配
        right = 0
        while right < n2 - left and words1[n1 - 1 - right] == words2[n2 - 1 - right]:
            right += 1

        return left + right >= n2
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将句子拆分为单词数组。较短的句子是较长的句子删除一段中间部分的结果。
# 使用双指针：从左边匹配公共前缀，从右边匹配公共后缀。
# 如果前缀+后缀覆盖了较短句子的所有单词，则相似。
# 等价于检查较短的句子是否完全由前缀和后缀组成。
#
# 时间复杂度: O(N) — N 为单词总数
# 空间复杂度: O(N) — 单词数组
#
# 关键点:
# - 插入的是连续的一段，所以匹配的是前缀和后缀
# - 不需要中间部分匹配
# - 必须保证较短句子的所有单词都能被前缀+后缀覆盖
