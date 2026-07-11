"""
LeetCode #792 - Number of Matching Subsequences
中文题名：匹配子序列的单词数
https://leetcode.com/problems/number-of-matching-subsequences/

Given string `S` and a dictionary of words `words`, find the
number of `words[i]` that is a subsequence of `S`.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in `words` that are a subsequence of `S`: "a", "acd", "ace".

Note:

All words in `words` and `S` will only consists of lowercase
letters.

The length of `S` will be in the range of `[1, 50000]`.

The length of `words` will be in the range of `[1, 5000]`.

The length of `words[i]` will be in the range of `[1, 50]`.

【中文翻译】
给定字符串 `S` 和一个单词字典 `words`，找出 `words[i]` 中是 `S` 的子序列的单词数量。

示例：
输入：
S = "abcde"
words = ["a", "bb", "acd", "ace"]
输出：3
解释：`words` 中有三个单词是 `S` 的子序列："a", "acd", "ace"。

注意：

`words` 和 `S` 中的所有单词只包含小写字母。

`S` 的长度范围是 `[1, 50000]`。

`words` 的长度范围是 `[1, 5000]`。

`words[i]` 的长度范围是 `[1, 50]`。
"""

from typing import List, Optional
from collections import defaultdict
import bisect


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # Build character -> sorted list of indices in S
        pos = defaultdict(list)
        for i, ch in enumerate(S):
            pos[ch].append(i)

        count = 0
        for word in words:
            cur_idx = -1
            match = True
            for ch in word:
                if ch not in pos:
                    match = False
                    break
                # Find the smallest index > cur_idx
                lst = pos[ch]
                nxt = bisect.bisect_right(lst, cur_idx)
                if nxt == len(lst):
                    match = False
                    break
                cur_idx = lst[nxt]
            if match:
                count += 1
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 预处理 + 二分查找。
# 如果对每个 word 都用双指针扫描 S，复杂度为 O(S + sum(len(words)))，当 words 很多时会较慢。
# 优化方法：预处理 S，构建每个字符到其出现位置列表的映射 char -> [index1, index2, ...]。
# 对每个 word，用二分查找依次确定每个字符在 S 中的下一个匹配位置：
# - 维护当前匹配到的 S 中的位置 cur_idx（初始为 -1）。
# - 对于 word 中的每个字符 ch，在 pos[ch] 列表中二分查找第一个 > cur_idx 的位置。
# - 如果找到，更新 cur_idx；如果未找到，说明该 word 不是子序列。
# 由于 S 可能较长（50000），words 较多（5000），此方法比逐字双指针更高效。
#
# 时间复杂度: O(S + W * L * log S)，其中 S 长度，W 是 words 数量，L 是每个 word 的平均长度
# 空间复杂度: O(S) - 存储字符位置映射
#
# 关键点:
# - 预处理字符位置映射以加速多次匹配
# - 二分查找每个字符的下一个可用位置
# - 也可以用"桶"方法：将 words 按下一个期望字符分组，遍历 S 一次处理所有 word
# - bisect_right 找到第一个 > cur_idx 的位置
