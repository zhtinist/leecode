"""
LeetCode #676 - Implement Magic Dictionary
中文题名：实现一个魔法字典
https://leetcode.com/problems/implement-magic-dictionary/

Implement a magic directory with `buildDict`, and `search` methods.

For the method `buildDict`, you'll be given a list of non-repetitive words to
build a dictionary.

For the method `search`, you'll be given a word, and judge whether if you modify
exactly one character into another character in this word, the modified word
is in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

Note:

You may assume that all the inputs are consist of lowercase letters `a-z`.

For contest purpose, the test data is rather small by now. You could think about highly
efficient algorithm after the contest.

Please remember to RESET your class variables declared in class MagicDictionary,
as static/class variables are persisted across multiple test cases. Please see here for more details.

【中文翻译】
实现一个魔法字典，包含 `buildDict` 和 `search` 两个方法。

对于方法 `buildDict`，你将得到一个不含重复单词的列表，用于构建字典。

对于方法 `search`，你将得到一个单词，判断如果将该单词中恰好一个字符修改为另一个字符，修改后的单词是否在你构建的字典中。

示例 1：

输入: buildDict(["hello", "leetcode"])，输出: Null
输入: search("hello")，输出: False
输入: search("hhllo")，输出: True
输入: search("hell")，输出: False
输入: search("leetcoded")，输出: False

注意：

你可以假设所有输入都由小写字母 `a-z` 组成。

为了竞赛目的，目前的测试数据规模较小。你可以在竞赛后考虑更高效的算法。

请记得重置你在 MagicDictionary 类中声明的类变量，因为静态/类变量会在多个测试用例之间持久化。
"""

from typing import List, Optional


class MagicDictionary:

    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        self.trie = {}
        for word in dictionary:
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = True

    def search(self, searchWord: str) -> bool:
        def dfs(node: dict, idx: int, modified: bool) -> bool:
            if idx == len(searchWord):
                return modified and '#' in node
            ch = searchWord[idx]
            if ch in node:
                if dfs(node[ch], idx + 1, modified):
                    return True
            if not modified:
                for nxt in node:
                    if nxt != '#' and nxt != ch:
                        if dfs(node[nxt], idx + 1, True):
                            return True
            return False

        return dfs(self.trie, 0, False)









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用字典树（Trie）存储所有单词。
# buildDict: 遍历每个单词，逐字符插入到 Trie 中，在单词结尾标记 '#'。
# search: 使用 DFS 递归搜索 Trie。
# - 在每个位置，如果当前字符匹配，可以继续向下匹配（不修改）。
# - 如果还没修改过字符，可以尝试跳到任意其他子节点（模拟修改一个字符）。
# - 到达单词末尾时，只有当恰好修改过一个字符且该位置是单词结尾时才返回 True。
#
# 时间复杂度: buildDict O(N*L) | search O(L*26^L) 最坏，但实际剪枝后远小于此
# 空间复杂度: O(N*L) - N 个单词，每个长度为 L，存储在 Trie 中
#
# 关键点:
# - 使用 Trie 高效存储和查找
# - DFS 带 modified 标志追踪是否已修改一个字符
# - 只有正好修改一个字符才算成功匹配
