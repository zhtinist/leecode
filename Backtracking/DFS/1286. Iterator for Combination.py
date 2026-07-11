"""
LeetCode #1286 - Iterator for Combination
中文题名：字母组合迭代器
https://leetcode.com/problems/iterator-for-combination/

Design an Iterator class, which has:

A constructor that takes a string `characters` of sorted
distinct lowercase English letters and a number `combinationLength`
as arguments.

A function next() that returns the next combination of length
`combinationLength` in lexicographical order.

A function hasNext() that returns `True` if and only if there
exists a next combination.

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

Constraints:

`1 <= combinationLength <= characters.length <= 15`

There will be at most `10^4` function calls per test.

It's guaranteed that all calls of the function `next` are
valid.

【中文翻译】
设计一个迭代器类，包含：

一个构造函数，接受一个由排序后的不同小写英文字母组成的字符串 characters 和一个数字 combinationLength 作为参数。
一个函数 next()，按字典序返回下一个长度为 combinationLength 的组合。
一个函数 hasNext()，当且仅当存在下一个组合时返回 True。

示例：

CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器。

iterator.next(); // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "bc"
iterator.hasNext(); // 返回 false

约束条件：

1 <= combinationLength <= characters.length <= 15
每次测试最多调用 10^4 次函数。
保证所有 next 调用都是有效的。
"""

from typing import List, Optional


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self._backtrack(characters, combinationLength, 0, [])
        self.index = 0

    def _backtrack(self, characters: str, length: int, start: int, path: List[str]):
        if len(path) == length:
            self.combinations.append(''.join(path))
            return
        for i in range(start, len(characters)):
            path.append(characters[i])
            self._backtrack(characters, length, i + 1, path)
            path.pop()

    def next(self) -> str:
        result = self.combinations[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 在构造函数中使用回溯法(Backtracking)预先生成所有组合。
# 由于 characters 已经排序，回溯过程中按顺序选择字符，
# 自然生成字典序排列的组合。将所有组合存储在一个列表中，
# 使用 index 指针跟踪当前迭代位置。
# next() 返回当前组合并移动指针，hasNext() 判断指针是否到达末尾。
#
# 时间复杂度: 构造 O(C(n, k) * k)，next() 和 hasNext() 均为 O(1)
# 空间复杂度: O(C(n, k) * k) - 存储所有组合
#
# 关键点:
# - 字符已排序，回溯按序选取保证字典序
# - 回溯剪枝：start 参数确保不重复选取同一字符
# - path 使用列表拼接而非字符串拼接以提高效率
