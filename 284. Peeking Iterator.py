"""
LeetCode #284 - Peeking Iterator
中文题名：窥视迭代器
https://leetcode.com/problems/peeking-iterator/

Given an Iterator class interface with methods: `next()` and
`hasNext()`, design and implement a PeekingIterator that support the
`peek()` operation -- it essentially peek() at the element that will be returned
by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: `[1,2,3]`.

Call `next()` gets you 1, the first element in the list.
Now you call `peek()` and it returns 2, the next element. Calling `next()` after that *still* return 2.
You call `next()` the final time and it returns 3, the last element.
Calling `hasNext()` after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not
just integer?

【中文翻译】
给定一个 Iterator 类接口，包含方法：`next()` 和 `hasNext()`，设计并实现一个支持 `peek()` 操作的 PeekingIterator——它本质上是在 `next()` 调用返回的元素之前进行窥视。

示例：

假设迭代器初始化到列表开头：`[1,2,3]`。

调用 `next()` 得到 1，列表中的第一个元素。
现在调用 `peek()` 返回 2，即下一个元素。之后调用 `next()` *仍然* 返回 2。
最后一次调用 `next()` 返回 3，即最后一个元素。
之后调用 `hasNext()` 应返回 false。

进阶：如何扩展你的设计使其通用，适用于所有类型，而不仅仅是整数？
"""

from typing import List, Optional


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    """Iterator that supports peek() operation.

    Cache the next element so peek() can return it without advancing.
    """

    def __init__(self, iterator):
        """Initialize with any iterator."""
        self.iterator = iterator
        self._next = None  # cached next element
        self._has_next = iterator.hasNext()
        if self._has_next:
            self._next = iterator.next()

    def peek(self):
        """Return the next element without advancing the iterator."""
        return self._next

    def next(self):
        """Return the next element and advance the iterator."""
        result = self._next
        if self.iterator.hasNext():
            self._next = self.iterator.next()
        else:
            self._next = None
            self._has_next = False
        return result

    def hasNext(self):
        """Return whether there are more elements."""
        return self._has_next


class Solution:
    """
    This problem uses PeekingIterator class, not Solution.
    The PeekingIterator implementation above is the complete solution.
    """
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 缓存下一个元素。在初始化时，调用底层迭代器的 hasNext() 和 next() 预先取出
# 下一个元素，缓存到 _next 变量中。
# - peek(): 直接返回缓存的 _next
# - next(): 返回 _next，然后调用底层迭代器获取下一个元素更新缓存
# - hasNext(): 返回 _has_next 标志
# 这样 peek() 操作不需要推进迭代器，只是读取缓存值。
#
# 时间复杂度: O(1) - peek(), next(), hasNext() 都是常数时间
# 空间复杂度: O(1) - 只缓存一个元素
#
# 关键点:
# - 核心思想是"预取"一个元素进行缓存
# - 初始化时需要主动调用底层迭代器的 next() 获取第一个元素
# - next() 返回缓存值后需要更新缓存
# - easy 扩展到泛型：缓存的类型设为泛型即可
