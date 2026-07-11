"""
LeetCode #1048 - Longest String Chain
中文题名：最长字符串链
https://leetcode.com/problems/longest-string-chain/

Given a list of words, each word consists of English lowercase letters.

Let's say `word1` is a predecessor of `word2` if and only if
we can add exactly one letter anywhere in `word1` to make it equal to
`word2`.  For example, `"abc"` is a
predecessor of `"abac"`.

A word chain is a sequence of words `[word_1, word_2, ..., word_k]` with
`k >= 1`, where `word_1` is a predecessor of
`word_2`, `word_2` is a predecessor of `word_3`, and so on.

Return the longest possible length of a word chain with words chosen from the given list of
`words`.

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

Note:

`1 <= words.length <= 1000`

`1 <= words[i].length <= 16`

`words[i]` only consists of English lowercase letters.

【中文翻译】
给定一个单词列表，每个单词由英文小写字母组成。

我们称 word1 是 word2 的前身当且仅当我们可以通过在 word1 的任意位置添加恰好一个字母使其等于 word2。例如，"abc" 是 "abac" 的前身。

词链是一个单词序列 [word_1, word_2, ..., word_k]，其中 k >= 1，word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。

返回从给定单词列表中选择单词可以组成的最长词链的长度。

示例 1：

输入：["a","b","ba","bca","bda","bdca"]
输出：4
解释：其中一个最长词链是 "a","ba","bda","bdca"。

注意：

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由英文小写字母组成。
"""

from typing import List, Optional


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by length (shortest first)
        words.sort(key=len)

        # dp[word] = longest chain ending at word
        dp = {}
        max_chain = 1

        for word in words:
            dp[word] = 1
            # Try removing each character to find a predecessor
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_chain = max(max_chain, dp[word])

        return max_chain










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划 + 排序。先将单词按长度从小到大排序，这样可以保证在处理每个单词时，
# 其所有可能的前身单词都已经被处理过。对于每个单词 word，尝试删除其中每个位置的字符
# 得到前身 predecessor。如果 predecessor 存在于 dp 中，则
# dp[word] = max(dp[word], dp[predecessor] + 1)。
# 初始化每个单词的链长为 1（只有自身）。
# 全局最大值即为答案。
#
# 时间复杂度: O(N * L^2) - N为单词数，L为单词最大长度（<=16）
#   排序O(N log N)，每个单词需要O(L)次删除操作，每次字符串拼接O(L)，总计O(N*L^2)
# 空间复杂度: O(N) - dp字典存储每个单词的链长
#
# 关键点:
# - 按长度排序确保前身一定在dp中
# - 删除每个位置的字符来生成前身
# - 每个单词的最大链长由其最长前身的链长+1得到
