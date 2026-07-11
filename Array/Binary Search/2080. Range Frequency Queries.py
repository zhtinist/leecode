"""
LeetCode #2080 - Range Frequency Queries
区间内查询数字的频率
https://leetcode.cn/problems/range-frequency-queries/

请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。
子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。
请你实现 `RangeFreqQuery` 类：
`RangeFreqQuery(int[] arr)` 用下标从 0 开始的整数数组 `arr` 构造一个类的实例。
`int query(int left, int right, int value)` 返回子数组 `arr[left...right]` 中 `value` 的 频率 。
一个 子数组 指的是数组中一段连续的元素。`arr[left...right]` 指的是 `nums` 中包含下标 `left` 和 `right` 在内 的中间一段连续元素。

示例 1：
输入： ["RangeFreqQuery", "query", "query"] [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]] 输出： [null, 1, 2]  解释： RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]); rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。 rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。

提示：
`1 <= arr.length <= 10^5`
`1 <= arr[i], value <= 10^4`
`0 <= left <= right < arr.length`
调用 `query` 不超过 `10^5` 次。
"""

from typing import List, Optional


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        from collections import defaultdict
        import bisect
        self.pos = defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        import bisect
        if value not in self.pos:
            return 0
        indices = self.pos[value]
        l = bisect.bisect_left(indices, left)
        r = bisect.bisect_right(indices, right)
        return r - l



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Segment Tree, Array, Hash Table, Binary Search
#
# 解题思路:
# 使用哈希表存储每个值在数组中的出现位置列表（有序）。对于查询[left, right, value]：
# 二分查找value的位置列表中第一个>=left的索引l和第一个>right的索引r。
# r-l即为value在区间内的出现次数。
#
# 时间复杂度: 构造O(n), 查询O(log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 哈希表+有序位置列表
# - 二分查找边界
# - bisect_left和bisect_right
