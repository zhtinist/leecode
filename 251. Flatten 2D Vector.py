"""
LeetCode #251 - Flatten 2D Vector
https://leetcode.com/problems/flatten-2d-vector/

Design and implement an iterator to flatten a 2d vector. It should support the following
operations: `next` and `hasNext`.

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false

Notes:

Please remember to RESET your class variables declared in Vector2D, as
static/class variables are persisted across multiple test cases. Please see here for more details.

You may assume that `next()` call will always be valid, that is, there will
be at least a next element in the 2d vector when `next()` is called.

Follow up:

As an added challenge, try to code it using only iterators
in C++ or iterators in Java.
"""

from typing import List, Optional


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0   # 当前行索引
        self.col = 0   # 当前列索引

    def _skip_empty(self):
        """跳过空行，移动到下一个有效位置"""
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        # 确保指向有效位置
        self._skip_empty()
        val = self.vec[self.row][self.col]
        self.col += 1
        return val

    def hasNext(self) -> bool:
        self._skip_empty()
        return self.row < len(self.vec)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 使用两个指针 row 和 col 跟踪当前在二维数组中的位置。
# 核心是 _skip_empty() 辅助方法：当 col 到达当前行末尾时，
# 自动跳到下一行非空行。next() 和 hasNext() 都先调用 _skip_empty
# 确保指针指向有效元素。hasNext() 在跳过空行后检查 row 是否越界。
#
# 时间复杂度: next()/hasNext() 均摊 O(1)
# 空间复杂度: O(1) — 只使用指针，不展开整个二维数组
#
# 关键点：
# - 不使用展开数组的方式，节省空间
# - _skip_empty 处理空行和行末跳转
# - next() 保证调用时 hasNext() 为 true（题目约定）
