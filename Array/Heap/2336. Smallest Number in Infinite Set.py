"""
LeetCode #2336 - Smallest Number in Infinite Set
无限集中的最小数字
https://leetcode.cn/problems/smallest-number-in-infinite-set/

现有一个包含所有正整数的集合 `[1, 2, 3, 4, 5, ...]` 。
实现 `SmallestInfiniteSet` 类：
`SmallestInfiniteSet()` 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。
`int popSmallest()` 移除 并返回该无限集中的最小整数。
`void addBack(int num)` 如果正整数 `num` 不 存在于无限集中，则将一个 `num` 添加 到该无限集中。

示例：
输入 ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"] [[], [2], [], [], [], [1], [], [], []] 输出 [null, null, 1, 2, 3, null, 1, 4, 5]  解释 SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet(); smallestInfiniteSet.addBack(2);    // 2 已经在集合中，所以不做任何变更。 smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 2 ，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 3 ，并将其从集合中移除。 smallestInfiniteSet.addBack(1);    // 将 1 添加到该集合中。 smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 在上一步中被添加到集合中，                                    // 且 1 是最小的整数，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 4 ，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 5 ，并将其从集合中移除。

提示：
`1 <= num <= 1000`
最多调用 `popSmallest` 和 `addBack` 方法 共计 `1000` 次
"""

from typing import List, Optional
import heapq


class SmallestInfiniteSet:
    """
    Maintain two pieces of state:
    1. self.next_num: the smallest positive integer that has never been popped.
    2. self.heap: a min-heap of numbers that were popped but added back.

    popSmallest():
        If the heap's top is smaller than next_num, pop from heap.
        Otherwise, return next_num and increment it.

    addBack(num):
        If num < next_num (already popped) and not currently in the heap,
        push it onto the heap.
    """

    def __init__(self):
        self.next_num = 1
        self.heap = []           # min-heap for numbers added back
        self.in_heap = set()     # tracks what's currently in the heap

    def popSmallest(self) -> int:
        if self.heap and self.heap[0] < self.next_num:
            num = heapq.heappop(self.heap)
            self.in_heap.remove(num)
            return num
        num = self.next_num
        self.next_num += 1
        return num

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Hash Table, Ordered Set, Heap (Priority Queue)
#
# 解题思路:
# 将"无限集合"分为两部分管理：
# 1. 未被弹出过的连续正整数序列，用 next_num 指针标记当前最小未弹出数。
# 2. 被弹出后又通过 addBack 加回来的数字，用小顶堆存储。
#
# popSmallest():
#   - 比较堆顶元素和 next_num：若堆顶更小，说明有之前弹出又被加回来的数，
#     从堆中弹出返回。
#   - 否则返回 next_num 并将指针后移。
#
# addBack(num):
#   - 只有当 num < next_num（即已被弹出过）且不在堆中时才加入堆。
#   - 使用集合 in_heap 去重，防止重复 addBack 同一数字。
#
# 时间复杂度:
#   - popSmallest(): O(log n) — 堆操作
#   - addBack(): O(log n) — 堆插入
#   - 总体 O(n log n)，n 为操作次数（最大 1000）
# 空间复杂度: O(n) — 堆和集合最多存储被 addBack 的元素数量
#
# 关键点:
# - next_num 指针标记"无限部分"的边界，避免存储所有正整数
# - 仅当 num < next_num 时 addBack 才有意义（num 已被弹出）
# - 集合 in_heap 防止重复添加同一数字到堆中
# - 堆顶与 next_num 的比较保证每次 popSmallest 返回全局最小值
