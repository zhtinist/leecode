"""
LeetCode #211 - Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters
`a-z` or `.`. A `.` means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:

You may assume that all words are consist of lowercase letters `a-z`.
"""

from typing import List, Optional


class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '#' in node
            ch = word[i]
            if ch == '.':
                for key in node:
                    if key != '#' and dfs(node[key], i + 1):
                        return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(node[ch], i + 1)

        return dfs(self.root, 0)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用字典实现的 Trie（前缀树）来存储单词，支持高效的前缀匹配。
# addWord: 将单词的每个字符逐层插入 Trie 节点，末尾用 '#' 标记单词结束。
# search: 使用 DFS 递归搜索。
#   - 遇到普通字母时，直接进入对应子节点。
#   - 遇到通配符 '.' 时，尝试当前节点的所有子节点（除 '#' 外）。
#   - 到达单词末尾时检查是否有结束标记 '#'。
#
# 时间复杂度: addWord O(L)，search 最坏 O(26^L) 当单词全为 '.' 时，平均远小于此
# 空间复杂度: O(N * L)，N 为单词数，L 为平均单词长度
#
# 关键点:
# - 使用嵌套字典实现 Trie，简洁且不需要定义 TrieNode 类
# - '#' 作为特殊键标记单词结束，避免在中间节点误判
# - DFS 遇到 '.' 时遍历所有子节点，需要跳过结束标记 '#'
