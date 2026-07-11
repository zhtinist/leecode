"""
LeetCode #820 - Short Encoding of Words
中文题名：单词的压缩编码
https://leetcode.com/problems/short-encoding-of-words/

Given a list of words, we may encode it by writing a reference string `S` and a
list of indexes `A`.

For example, if the list of words is `["time", "me", "bell"]`,
we can write it as `S = "time#bell#"` and `indexes = [0, 2,
5]`.

Then for each index, we will recover the word by reading from the reference string from that
index until we reach a `"#"` character.

What is the length of the shortest reference string S possible that encodes the given
words?

Example:

Input: words = `["time", "me", "bell"]`
Output: 10
Explanation: S = `"time#bell#" and indexes = [0, 2, 5`].

Note:

`1 <= words.length <= 2000`.

`1 <= words[i].length <= 7`.

Each word has only lowercase letters.

【中文翻译】
给定一个单词列表，我们可以通过写出一个参考字符串 `S` 和一个索引列表 `A` 来进行编码。

例如，如果单词列表是 `["time", "me", "bell"]`，我们可以写成 `S = "time#bell#"` 和 `indexes = [0, 2, 5]`。

然后对于每个索引，我们将通过从参考字符串的该索引开始读取直到遇到 `"#"` 字符来恢复单词。

给定单词列表，可能的编码最短参考字符串 S 的长度是多少？

示例：
输入：words = `["time", "me", "bell"]`
输出：10
解释：S = `"time#bell#"`，indexes = `[0, 2, 5]`。

注意：
`1 <= words.length <= 2000`。
`1 <= words[i].length <= 7`。
每个单词只包含小写字母。
"""

from typing import List, Optional


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word_set = set(words)
        for word in words:
            # Remove all suffixes of this word from the set
            for i in range(1, len(word)):
                suffix = word[i:]
                word_set.discard(suffix)
        # Each remaining word needs len(word) + 1 characters (word + '#')
        return sum(len(w) + 1 for w in word_set)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 核心洞察：如果单词 A 是单词 B 的后缀，那么 A 可以
# 作为 B 编码的一部分，不需要独立存储。
# 例如 "me" 是 "time" 的后缀，S = "time#..." 中
# 索引 2 处可以恢复 "me"。
#
# 算法：
# 1. 将所有单词放入哈希集合。
# 2. 遍历每个单词，检查它的所有后缀（从位置 1 开始），
#    如果后缀也存在于集合中，则移除它。
# 3. 最终集合中剩余的单词是必须独立编码的单词，
#    每个单词需要 len(word) + 1 个字符（带 '#' 终止符）。
#
# 时间复杂度: O(N * L) - N 个单词，每个长度 L <= 7
# 空间复杂度: O(N * L) - 存储单词集合
#
# 关键点:
# - 后缀关系决定是否可以共享编码
# - set.discard 避免 KeyError
# - 每个保留的单词贡献 len + 1 的长度
# - 另一种解法：后缀 Trie（字典树）
