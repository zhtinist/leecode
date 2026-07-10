"""
LeetCode #212 - Word Search II
中文题名：单词搜索 II
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically neighboring. The same letter cell may not be used
more than once in a word.

Example:

Input:
board = [
['o','a','a','n'],
['e','t','a','e'],
['i','h','k','r'],
['i','f','l','v']
]
words = `["oath","pea","eat","rain"]`

Output: `["eat","oath"]`

Note:

All inputs are consist of lowercase letters `a-z`.

The values of `words` are distinct.

【中文翻译】
给定一个二维 board 和一个字典中的单词列表，找出所有同时在二维 board 和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中「相邻」单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例：

输入：
board = [
['o','a','a','n'],
['e','t','a','e'],
['i','h','k','r'],
['i','f','l','v']
]
words = `["oath","pea","eat","rain"]`

输出：`["eat","oath"]`

注意：

所有输入都由小写字母 `a-z` 组成。

`words` 中的值互不相同。
"""

from typing import List, Optional


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = word

        m, n = len(board), len(board[0])
        result = []

        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node:
                return

            curr = node[ch]
            # Check if we found a word
            word_match = curr.get('#')
            if word_match:
                result.append(word_match)
                del curr['#']  # Avoid duplicates

            # Mark visited
            board[i][j] = '#'

            # Explore neighbors
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, curr)

            # Restore
            board[i][j] = ch

            # Prune empty nodes for optimization
            if not curr:
                del node[ch]

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 结合 Trie（前缀树）和 DFS 回溯来解决二维网格中的多单词搜索问题。
# 1. 将所有待搜索单词构建成 Trie，值存储完整单词便于快速获取结果。
# 2. 遍历 board 的每个单元格作为起点，进行 DFS 搜索。
# 3. 在 DFS 中，检查当前字符是否在 Trie 节点中，若不在则剪枝返回。
# 4. 找到单词后立即从 Trie 中删除结束标记，避免重复结果。
# 5. 使用 board 原地标记访问（临时改为 '#'），回溯时恢复。
# 6. 搜索完一个节点后，若其子节点为空则向上删除该节点进行后序剪枝优化。
#
# 时间复杂度: O(M * N * 4^L)，M,N 为 board 尺寸，L 为最长单词长度（Trie 剪枝后实际远小于此）
# 空间复杂度: O(W * L)，W 为单词数，L 为平均长度（Trie 存储），递归栈深度 O(L)
#
# 关键点:
# - Trie 剪枝：当前字符不在 Trie 中时立即返回，大幅减少无效搜索
# - 原地标记访问：将 board[i][j] 临时改为 '#'，避免额外 visited 数组
# - 删除已匹配单词：找到单词后删除 '#' 标记，防止重复添加到结果
# - 后序剪枝：搜索完子节点后若节点为空则向上删除，进一步优化后续搜索
