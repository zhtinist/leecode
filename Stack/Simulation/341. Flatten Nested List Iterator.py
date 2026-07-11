"""
LeetCode #341 - Flatten Nested List Iterator
中文题名：扁平化嵌套列表迭代器
https://leetcode.com/problems/flatten-nested-list-iterator/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other
lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: `[1,1,2,1,1]`.

Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: `[1,4,6]`.

【中文翻译】
给你一个嵌套的整数列表 nestedList。请你实现一个迭代器将其扁平化，使其能够遍历这个列表中的所有整数。

列表中的每个元素要么是一个整数，要么是一个列表——该列表的元素也可能是整数或其他列表。

示例 1：

输入：[[1,1],2,[1,1]]
输出：[1,1,2,1,1]
解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是：[1,1,2,1,1]。

示例 2：

输入：[1,[4,[6]]]
输出：[1,4,6]
解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是：[1,4,6]。
"""

from typing import List, Optional


class NestedIterator:
    def __init__(self, nestedList: List['NestedInteger']):
        self.stack = []
        # Push the reversed list onto the stack
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        self._ensure_integer_on_top()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self._ensure_integer_on_top()
        return len(self.stack) > 0

    def _ensure_integer_on_top(self):
        while self.stack and not self.stack[-1].isInteger():
            nested = self.stack.pop()
            nested_list = nested.getList()
            for i in range(len(nested_list) - 1, -1, -1):
                self.stack.append(nested_list[i])











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈（stack）惰性展开嵌套列表：
# 1. 初始化时将整个嵌套列表逆序压入栈中。
# 2. _ensure_integer_on_top() 确保栈顶元素是一个整数：
#    如果栈顶是嵌套列表，弹出它并将该列表的所有元素逆序压入栈中（重复此过程直到栈顶是整数）。
# 3. next()：调用 _ensure_integer_on_top() 后弹出栈顶整数并返回。
# 4. hasNext()：调用 _ensure_integer_on_top() 后返回栈是否非空。
# 惰性展开的优点：不需要一次性展开所有元素，只在需要时才展开下一层，节省空间。
#
# 时间复杂度:
# - 构造器：O(n)，n 为嵌套列表的顶层元素个数
# - next() / hasNext()：均摊 O(1)，每个元素最多被处理一次
# 空间复杂度: O(D + L)，
# - D 为嵌套深度（栈中最多同时存 D 层未完全展开的列表），L 为任意一层的最大元素数
#
# 关键点:
# - 惰性展开（lazy flattening）：只在需要时展开，而非一次性全展开
# - 使用栈逆序存储元素和子列表
# - 类名为 NestedIterator 而非 Solution（LeetCode 要求）
# - 实现 NestedInteger 接口的方法：isInteger(), getInteger(), getList()
