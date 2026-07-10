"""
LeetCode #295 - Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. If the size of the list is even, there
is no middle value. So the median is the mean of the two middle value.

For example,

`[2,3,4]`, the median is `3`

`[2,3]`, the median is `(2 + 3) / 2 = 2.5`

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data
structure.

double findMedian() - Return the median of all elements so far.

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you
optimize it?

If 99% of all integer numbers from the stream are between 0 and 100, how would you
optimize it?
"""

from typing import List, Optional


import heapq


class MedianFinder:
    """Data structure that supports adding numbers and finding median.

    Two-heap approach:
    - max_heap (left half): stores the smaller half of numbers (negated for max-heap)
    - min_heap (right half): stores the larger half of numbers

    Invariant: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
    Median:
    - If sizes equal: average of both heap tops
    - If max_heap larger: top of max_heap
    """

    def __init__(self):
        self.max_heap = []  # smaller half (negated, so top is the largest of small half)
        self.min_heap = []  # larger half

    def addNum(self, num: int) -> None:
        """Add a number to the data structure."""
        # Always add to max_heap first (smaller half)
        heapq.heappush(self.max_heap, -num)

        # Move the largest element of max_heap to min_heap
        largest_of_small = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, largest_of_small)

        # Balance: keep max_heap size >= min_heap size
        if len(self.max_heap) < len(self.min_heap):
            smallest_of_large = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest_of_large)

    def findMedian(self) -> float:
        """Return the median of all elements."""
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


class Solution:
    """
    This problem uses MedianFinder class, not Solution.
    The MedianFinder implementation above is the complete solution.
    """
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 使用两个堆维护数据流的中位数：
# - 最大堆（max_heap）：存储较小的一半数字（Python 的 heapq 是最小堆，所以存负数）
# - 最小堆（min_heap）：存储较大的一半数字
#
# 添加数字时：
# 1. 先将新数字加入 max_heap（较小的一半）
# 2. 将 max_heap 的最大值移到 min_heap（保持两个堆的正确划分）
# 3. 如果 min_heap 比 max_heap 大，将 min_heap 的最小值移回 max_heap
#
# 维持不变量：len(max_heap) == len(min_heap) 或 len(max_heap) == len(min_heap) + 1
# 中位数：
# - 两堆大小相等：(max_heap 堆顶 + min_heap 堆顶) / 2
# - max_heap 更大：max_heap 堆顶
#
# 时间复杂度: addNum O(log N), findMedian O(1)
# 空间复杂度: O(N) - 两个堆存储所有元素
#
# 关键点:
# - Python heapq 是最小堆，最大堆通过存负数实现
# - 添加流程的三步操作维持平衡
# - 不需要每次都完全排序，只需维护两个堆的有序划分
# - Follow up: 如果数据在 0-100 可以计数排序，O(1) 查找
