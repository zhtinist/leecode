"""
LeetCode #281 - Zigzag Iterator
https://leetcode.com/problems/zigzag-iterator/

Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]

Output: `[1,3,2,4,5,6]

Explanation:` By calling *next* repeatedly until *hasNext* returns `false`,
the order of elements returned by *next* should be: `[1,3,2,4,5,6]`.

Follow up: What if you are given `k` 1d vectors? How well can your code be
extended to such cases?

Clarification for the follow up question:

The "Zigzag" order is not clearly defined and is ambiguous for `k >
2` cases. If "Zigzag" does not look right to you, replace "Zigzag"
with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: `[1,4,8,2,5,9,3,6,7]`.
"""

from typing import List, Optional


class ZigzagIterator:
    """Iterator that returns elements from multiple 1D vectors in alternating order.

    Uses a queue to track which vector to read from next.
    Stores vectors and current index for each, cycling through the queue.
    """

    def __init__(self, v1: List[int], v2: List[int]):
        from collections import deque
        self.queue = deque()
        self.vectors = [v1, v2]
        self.indices = [0, 0]
        # Add non-empty vectors to queue
        if v1:
            self.queue.append(0)
        if v2:
            self.queue.append(1)

    def next(self) -> int:
        """Return the next element in zigzag order."""
        vec_idx = self.queue.popleft()
        val = self.vectors[vec_idx][self.indices[vec_idx]]
        self.indices[vec_idx] += 1
        # If this vector still has elements, put it back at end of queue
        if self.indices[vec_idx] < len(self.vectors[vec_idx]):
            self.queue.append(vec_idx)
        return val

    def hasNext(self) -> bool:
        """Return whether there are more elements."""
        return len(self.queue) > 0


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 使用队列管理多个向量。初始化时将所有非空向量的迭代器加入队列。
# next(): 从队列头部取出一个迭代器，返回其下一个元素，如果该迭代器还有剩余
# 元素则将其放回队列尾部。
# hasNext(): 检查队列是否非空。
#
# 对于 k 个向量的扩展，只需初始化时将 k 个非空向量的迭代器全部加入队列即可。
# 队列的轮转保证了交替（循环）顺序。
#
# 时间复杂度: O(1) - next() 和 hasNext() 都是 O(1)
# 空间复杂度: O(K) - 队列最多存放 K 个迭代器
#
# 关键点:
# - 使用队列（deque）实现轮转访问
# - 每个向量用一个独立的迭代器
# - 初始化时跳过空向量
# - 迭代器耗尽后不再放回队列
# - 可以自然地扩展到 k 个向量
