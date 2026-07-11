"""
LeetCode #318 - Maximum Product of Word Lengths
中文题名：最大单词长度乘积
https://leetcode.com/problems/maximum-product-of-word-lengths/

Given a string array `words`, find the maximum value of `length(word[i]) *
length(word[j])` where the two words do not share common letters. You may assume that
each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: `["abcw","baz","foo","bar","xtfn","abcdef"]`
Output: `16
Explanation: `The two words can be `"abcw", "xtfn"`.

Example 2:

Input: `["a","ab","abc","d","cd","bcd","abcd"]`
Output: `4
Explanation: `The two words can be `"ab", "cd"`.

Example 3:

Input: `["a","aa","aaa","aaaa"]`
Output: `0
Explanation: `No such pair of words.

【中文翻译】
给定一个字符串数组 words，找出 length(word[i]) * length(word[j]) 的最大值，其中这两个单词
不包含公共字母。你可以假设每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1：

输入：["abcw","baz","foo","bar","xtfn","abcdef"]
输出：16
解释：这两个单词可以是 "abcw" 和 "xtfn"。

示例 2：

输入：["a","ab","abc","d","cd","bcd","abcd"]
输出：4
解释：这两个单词可以是 "ab" 和 "cd"。

示例 3：

输入：["a","aa","aaa","aaaa"]
输出：0
解释：不存在这样的两个单词。
"""

from typing import List, Optional


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 为每个单词计算位掩码和长度
        masks = []
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks.append((mask, len(word)))
        res = 0
        n = len(masks)
        # 两两比较所有单词对
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i][0] & masks[j][0] == 0:
                    res = max(res, masks[i][1] * masks[j][1])
        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 位掩码（Bitmask）+ 枚举。由于只有 26 个小写字母，可以用一个 32 位整数表示一个单词中出现的
# 字母集合：第 (ch - 'a') 位为 1 表示该字母在单词中出现过。
# 预处理每个单词的掩码 mask 和长度，然后两两比较所有单词对：
# 如果 mask[i] & mask[j] == 0，说明两个单词没有公共字母，计算长度乘积并更新最大值。
# 位运算的 AND 操作 O(1) 即可判断两个单词是否有公共字母。
#
# 时间复杂度: O(N^2 + L) - N 是单词数量，L 是所有单词的总长度（用于计算掩码）
# 空间复杂度: O(N) - 存储每个单词的 (mask, length) 元组
#
# 关键点:
# - 位掩码高效判断字符集是否有交集：mask_i & mask_j == 0
# - 26 个字母只需 26 位，32 位整数足够
# - 预处理掩码避免重复遍历单词字符
# - 输出的是长度乘积的最大值，不是单词本身
