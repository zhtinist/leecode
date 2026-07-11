"""
LeetCode #2054 - Two Best Non-Overlapping Events
两个最好的不重叠活动
https://leetcode.cn/problems/two-best-non-overlapping-events/

给你一个下标从 0 开始的二维整数数组 `events` ，其中 `events[i] = [startTime_i, endTime_i, value_i]` 。第 `i` 个活动开始于 `startTime_i` ，结束于 `endTime_i` ，如果你参加这个活动，那么你可以得到价值 `value_i` 。你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。
请你返回价值之和的 最大值 。
注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 `t` ，那么下一个活动必须在 `t + 1` 或之后的时间开始。

示例 1:

输入：events = [[1,3,2],[4,5,2],[2,4,3]] 输出：4 解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。
示例 2：

输入：events = [[1,3,2],[4,5,2],[1,5,5]] 输出：5 解释：选择活动 2 ，价值和为 5 。
示例 3：

输入：events = [[1,5,3],[1,5,1],[6,6,5]] 输出：8 解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。

提示：
`2 <= events.length <= 10^5`
`events[i].length == 3`
`1 <= startTime_i <= endTime_i <= 10^9`
`1 <= value_i <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        n = len(events)

        # Precompute suffix maximum values (max value from index i to end)
        suffix_max = [0] * n
        suffix_max[-1] = events[-1][2]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(events[i][2], suffix_max[i + 1])

        result = 0
        for i in range(n):
            # Option 1: Use only this event
            result = max(result, events[i][2])

            # Option 2: Try to pair with a non-overlapping event after this one
            # Binary search for the first event that starts after events[i].end
            target = events[i][1] + 1  # must start after end
            left, right = i + 1, n - 1
            pos = n
            while left <= right:
                mid = (left + right) // 2
                if events[mid][0] >= target:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if pos < n:
                result = max(result, events[i][2] + suffix_max[pos])

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Dynamic Programming, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 按开始时间排序events。预计算后缀最大值数组suffix_max[i]：
# 从i开始到末尾的最大value。对于每个事件i，尝试两种情况：
# 1) 只选这一个事件；2) 选i + 二分搜索找到第一个开始时间大于i结束时间的事件，
# 加上其后缀最大值。取所有情况的最大值。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 按开始时间排序
# - 后缀最大值数组预计算
# - 二分查找不重叠的下一个事件
