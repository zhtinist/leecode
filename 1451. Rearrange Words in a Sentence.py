"""
LeetCode #1451 - Rearrange Words in a Sentence
中文题名：重新排列句子中的单词
https://leetcode.com/problems/rearrange-words-in-a-sentence/

Given a sentence `text` (A sentence is a string
of space-separated words) in the following format:

First letter is in upper case.

Each word in `text` are separated by a single space.

Your task is to rearrange the words in text such that all words are rearranged
in an increasing order of their lengths. If two words have the same length, arrange
them in their original order.

Return the new text following the format shown above.

Example 1:

Input: text = "Leetcode is cool"
Output: "Is cool leetcode"
Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.

Example 2:

Input: text = "Keep calm and code on"
Output: "On and keep calm code"
Explanation: Output is ordered as follows:
"On" 2 letters.
"and" 3 letters.
"keep" 4 letters in case of tie order by position in original text.
"calm" 4 letters.
"code" 4 letters.

Example 3:

Input: text = "To be or not to be"
Output: "To be or to be not"

Constraints:

`text` begins with a capital letter and then contains lowercase
letters and single space between words.

`1 <= text.length <= 10^5`

【中文翻译】
给定一个句子 `text`（句子由空格分隔的单词组成），格式如下：

首字母大写。

`text` 中的每个单词由单个空格分隔。

你的任务是重新排列句子中的单词，使所有单词按长度递增顺序排列。如果两个单词长度相同，
则保持它们在原始句子中的相对顺序。

返回按上述格式重新排列后的新句子。

示例 1：

输入：text = "Leetcode is cool"
输出："Is cool leetcode"
解释：有 3 个单词，"Leetcode" 长度为 8，"is" 长度为 2，"cool" 长度为 4。
输出按长度排序，并且新的第一个单词以大写字母开头。

示例 2：

输入：text = "Keep calm and code on"
输出："On and keep calm code"
解释：输出顺序如下：
"On" 2 个字母。
"and" 3 个字母。
"keep" 4 个字母，平局时按原始文本中的顺序排列。
"calm" 4 个字母。
"code" 4 个字母。

示例 3：

输入：text = "To be or not to be"
输出："To be or to be not"

约束条件：

`text` 以大写字母开头，然后包含小写字母，单词之间由单个空格分隔。

`1 <= text.length <= 10^5`
"""

from typing import List, Optional


class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words.sort(key=len)
        result = " ".join(words).lower()
        return result[0].upper() + result[1:]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将句子按空格分割成单词列表。Python 的 sort(key=len) 是稳定排序，
# 因此相同长度的单词会保持原始顺序。
# 排序后，将所有单词转为小写并用空格连接。
# 最后将结果字符串的首字母大写，其余保持小写，符合题目要求的输出格式。
#
# 时间复杂度: O(N log N)  -- 排序占主导，N 为单词数量
# 空间复杂度: O(N)  -- 存储分割后的单词列表
#
# 关键点:
# - Python 的 sort 是稳定排序，能自动满足"相同长度保持原始顺序"的要求
# - 原始句子首字母大写，排序后全部转小写再首字母大写
# - 题目要求输出格式：首字母大写，其余小写，单词间单空格分隔









