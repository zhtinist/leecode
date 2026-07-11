"""
LeetCode #648 - Replace Words
中文题名：单词替换
https://leetcode.com/problems/replace-words/

In English, we have a concept called `root`, which can be followed by some other
words to form another longer word - let's call this word `successor`. For
example, the root `an`, followed by `other`, which can form another
word `another`.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the
`successor` in the sentence with the `root` forming it. If a `successor`
has many `roots` can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:

The input will only have lower-case letters.

1 <= dict words number <= 1000

1 <= sentence words number <= 1000

1 <= root length <= 100

1 <= sentence words length <= 1000

【中文翻译】
在英语中，我们有一个叫做「词根」(root) 的概念，它可以后接一些其他单词来形成另一个更长的单词——我们称这个更长的单词为「继承词」(successor)。例如，词根 `an`，后接 `other`，可以形成另一个单词 `another`。

现在，给定一个由许多词根组成的字典和一个句子。你需要将句子中的所有「继承词」用「词根」替换掉。如果一个「继承词」有多个「词根」可以构成它，则用最短的词根替换它。

你需要输出替换之后的句子。

示例 1：

输入：dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

注意：

输入只包含小写字母。

1 <= 字典单词数 <= 1000

1 <= 句子单词数 <= 1000

1 <= 词根长度 <= 100

1 <= 句子单词长度 <= 1000
"""

from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.is_word = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

        words = sentence.split()
        result: list[str] = []

        for word in words:
            node = root
            prefix: list[str] = []
            found = False
            for ch in word:
                if ch not in node.children:
                    break
                prefix.append(ch)
                node = node.children[ch]
                if node.is_word:
                    result.append(''.join(prefix))
                    found = True
                    break
            if not found:
                result.append(word)

        return ' '.join(result)











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用字典树（Trie）存储所有词根。对于句子中的每个单词，在 Trie 中逐字符查找，
# 一旦遇到一个标记为词根的节点，就用该词根替换原单词。
# 如果遍历完单词也没有找到词根，则保留原单词。
# 最后用空格连接所有处理后的单词返回。
#
# 时间复杂度: O(N * L) - 其中 N 是句子中的单词数，L 是单词的平均长度。
#           构建 Trie 需要 O(D * W)，其中 D 是字典大小，W 是词根平均长度。
# 空间复杂度: O(D * W) - Trie 存储所有词根字符
#
# 关键点:
# - 前缀树的典型应用场景：查找最短前缀匹配
# - 题目要求用最短的词根替换，因此一旦找到词根就立即停止搜索
# - 如果找不到任何词根前缀，保留原单词
# - 也可用字符串 startswith 暴力匹配，但 Trie 更高效
