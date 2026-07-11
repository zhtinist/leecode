"""
LeetCode #677 - Map Sum Pairs
中文题名：键值映射
https://leetcode.com/problems/map-sum-pairs/

Implement a MapSum class with `insert`, and `sum` methods.

For the method `insert`, you'll be given a pair of (string, integer). The string
represents the key and the integer represents the value. If the key already existed, then
the original key-value pair will be overridden to the new one.

For the method `sum`, you'll be given a string representing the prefix, and you
need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:

Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5

【中文翻译】
实现一个 MapSum 类，包含 `insert` 和 `sum` 两个方法。

对于方法 `insert`，你将得到一个 (字符串, 整数) 键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被新的键值对覆盖。

对于方法 `sum`，你将得到一个表示前缀的字符串，需要返回所有键以该前缀开头的键值对的值之和。

示例 1：

输入: insert("apple", 3)，输出: Null
输入: sum("ap")，输出: 3
输入: insert("app", 2)，输出: Null
输入: sum("ap")，输出: 5
"""

from typing import List, Optional


class MapSum:

    def __init__(self):
        self.trie = {}
        self.val = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.val.get(key, 0)
        self.val[key] = val
        node = self.trie
        for ch in key:
            if ch not in node:
                node[ch] = {'_sum': 0}
            node = node[ch]
            node['_sum'] += delta

    def sum(self, prefix: str) -> int:
        node = self.trie
        for ch in prefix:
            if ch not in node:
                return 0
            node = node[ch]
        return node['_sum']









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用字典树（Trie）的变体，每个节点维护一个 _sum 值表示经过该节点的所有键的值之和。
# insert: 先计算 delta（新值与旧值的差，若键不存在则旧值为 0）。
# 然后遍历 key 的每个字符，在对应 Trie 节点上将 _sum 加上 delta。
# 同时用 val 字典记录每个 key 对应的当前值，用于处理键的重复插入（覆盖）。
# sum: 遍历 prefix 到达对应节点后，直接返回该节点的 _sum 值。
#
# 时间复杂度: insert O(L) | sum O(L) - L 为 key/prefix 的长度
# 空间复杂度: O(N*L) - N 个键，每个长度为 L
#
# 关键点:
# - 每个 Trie 节点维护 _sum 值为经过该节点的所有键的值的总和
# - 使用 delta 增量更新处理键值覆盖
# - val 字典记录每个键的当前值以支持覆盖操作
