"""
LeetCode #900 - RLE Iterator
中文题名：RLE 迭代器
https://leetcode.com/problems/rle-iterator/

Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by `RLEIterator(int[] A)`, where `A` is a
run-length encoding of some sequence.  More specifically, for all even `i`, `A[i]`
tells us the number of times that the non-negative integer value `A[i+1]` is
repeated in the sequence.

The iterator supports one function: `next(int n)`, which exhausts the next
`n` elements (`n >= 1`) and returns the last element exhausted
in this way.  If there is no element left to exhaust, `next` returns
`-1` instead.

For example, we start with `A = [3,8,0,9,2,5]`, which is a run-length encoding of
the sequence `[8,8,8,5,5]`.  This is because the sequence can be read as "three
eights, zero nines, two fives".

Example 1:

Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
Output: [null,8,8,5,-1]
Explanation:
RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
This maps to the sequence [8,8,8,5,5].
RLEIterator.next is then called 4 times:

.next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].

.next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].

.next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].

.next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
but the second term did not exist.  Since the last term exhausted does not exist, we return -1.

Note:

`0 <= A.length <= 1000`

`A.length` is an even integer.

`0 <= A[i] <= 10^9`

There are at most `1000` calls to `RLEIterator.next(int n)` per
test case.

Each call to `RLEIterator.next(int n)` will have `1 <= n
<= 10^9`.

【中文翻译】
编写一个遍历游程编码序列的迭代器。

迭代器由 `RLEIterator(int[] A)` 初始化，其中 `A` 是某个序列的游程编码。具体来说，对于所有偶数 `i`，`A[i]` 告诉我们在序列中非负整数值 `A[i+1]` 重复的次数。

迭代器支持一个函数：`next(int n)`，它消耗接下来的 `n` 个元素（`n >= 1`）并返回以此方式消耗的最后一个元素。如果没有剩余元素可以消耗，则 `next` 返回 `-1`。

例如，假设 `A = [3,8,0,9,2,5]`，这是序列 `[8,8,8,5,5]` 的游程编码。因为该序列可以解读为"三个 8，零个 9，两个 5"。

示例 1：

输入：["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
输出：[null,8,8,5,-1]
解释：
RLEIterator 由 RLEIterator([3,8,0,9,2,5]) 初始化。
这对应序列 [8,8,8,5,5]。
然后调用 RLEIterator.next 4 次：

.next(2) 消耗序列的 2 项，返回 8。剩余序列为 [8,5,5]。

.next(1) 消耗序列的 1 项，返回 8。剩余序列为 [5,5]。

.next(1) 消耗序列的 1 项，返回 5。剩余序列为 [5]。

.next(2) 消耗 2 项，返回 -1。因为消耗的第一项是 5，但第二项不存在。由于最后一个消耗的元素不存在，我们返回 -1。

"""

from typing import List, Optional


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.A = encoding
        self.idx = 0          # 当前偶数的索引（指向计数值）
        self.remaining = 0    # 当前元素剩余的个数

    def next(self, n: int) -> int:
        while self.idx < len(self.A) and n > self.remaining:
            n -= self.remaining          # 消耗掉当前剩余的
            self.idx += 2                # 跳到下一组
            if self.idx < len(self.A):
                self.remaining = self.A[self.idx]

        if self.idx >= len(self.A):
            return -1

        self.remaining -= n
        return self.A[self.idx + 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用指针 idx 追踪当前计数值的位置（偶数索引），remaining 追踪当前值还剩多少未消耗。
# 每次 next(n)：
# 1. 若 n > remaining，说明需要跳过当前组。n -= remaining，idx += 2 移到下一组。
# 2. 若 idx 已经越界，返回 -1。
# 3. 否则 remaining -= n，返回当前值 A[idx+1]。
#
# 跳过计数为 0 的组是自然的：remaining 初始为 0，第一次 while 循环就会跳过。
#
# 时间复杂度: O(N) — 每个元素对 (count, value) 最多被访问一次
# 空间复杂度: O(1) — 只使用固定变量
#
# 关键点:
# - 不需要展开整个序列，直接操作游程编码
# - 使用 while 循环处理跳过多个完整组的情况
# - remaining 的初始值和更新时机要仔细处理
