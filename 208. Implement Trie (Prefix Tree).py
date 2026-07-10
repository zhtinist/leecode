"""
LeetCode #208 - Implement Trie (Prefix Tree)
中文题名：实现 Trie（前缀树）
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with `insert`, `search`, and `startsWith`
methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:

You may assume that all inputs are consist of lowercase letters `a-z`.

All inputs are guaranteed to be non-empty strings.

【中文翻译】
实现 Trie（前缀树），包含 `insert`、`search` 和 `startsWith` 这三个操作。

示例：

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

注意：

你可以假设所有的输入都是由小写字母 `a-z` 组成的。

所有输入均保证为非空字符串。
"""

from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 实现字典树（Trie / Prefix Tree）。使用 TrieNode 节点类：
# - children：字典存储子节点，键为字符，值为 TrieNode
# - is_end：标记该节点是否为一个完整单词的结尾
#
# 三个操作：
# 1. insert(word)：沿 root 遍历每个字符，不存在则创建新节点。最后标记 is_end = True
# 2. search(word)：沿 root 遍历，若中途字符不存在返回 False，最后检查 is_end
# 3. startsWith(prefix)：类似 search 但不检查 is_end，只要能走完 prefix 所有字符即可
#
# 时间复杂度: O(L) — 每个操作都是 O(L)，L 为单词长度
# 空间复杂度: O(N * L) — 所有插入单词的总字符数
#
# 关键点:
# - search 和 startsWith 的区别在于是否检查 is_end
# - children 用字典比固定数组更节省空间（只需存储实际出现的字符）
# - 另一种实现：用长度为 26 的数组存储子节点（适用于纯小写字母）
