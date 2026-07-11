"""
LeetCode #435 - Non-overlapping Intervals
中文题名：无重叠区间
https://leetcode.com/problems/non-overlapping-intervals/

Given a collection of intervals, find the minimum number of intervals you need to remove to
make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:

You may assume the interval's end point is always bigger than its start point.

Intervals like [1,2] and [2,3] have borders "touching" but they don't
overlap each other.

【中文翻译】
给定一个区间集合，找出需要移除的最小区间数量，使剩余区间互不重叠。

示例 1：
    输入：[[1,2],[2,3],[3,4],[1,3]]
    输出：1
    解释：移除 [1,3] 后，剩余区间互不重叠。

示例 2：
    输入：[[1,2],[1,2],[1,2]]
    输出：2
    解释：需要移除两个 [1,2] 才能使剩余区间不重叠。

示例 3：
    输入：[[1,2],[2,3]]
    输出：0
    解释：不需要移除任何区间，它们已经互不重叠。

注意：
    区间终点始终大于起点。
    [1,2] 和 [2,3] 边界接触但不重叠。
"""

from typing import List, Optional


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                removals += 1  # Overlap, remove current interval
            else:
                prev_end = end  # No overlap, update prev_end

        return removals


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法。按区间结束时间升序排列。
#
# 核心思想：为了保留最多的区间，每次选择结束时间最早的区间。
# 这样可以为后续区间留出最大的空间，从而最小化移除数量。
#
# 算法步骤：
# 1. 按 end 升序排序区间
# 2. 维护 prev_end（上一个保留区间的结束时间）
# 3. 遍历剩余区间：
#    - 如果当前区间的 start < prev_end，说明重叠，移除当前区间（count++）
#    - 否则，无重叠，更新 prev_end = 当前区间的 end
#
# 这实际上是经典的"区间调度"问题——选择最多的不重叠区间。
# 需要移除的数量 = 总区间数 - 最多可保留的区间数。
#
# 时间复杂度: O(N log N) — 排序
# 空间复杂度: O(1) — 只使用常数变量（不计排序所需栈空间）
#
# 关键点:
# - 按结束时间排序是关键，不能按开始时间排序
# - 贪心选择最早结束的区间
# - 等价于：总区间数 - 最多不重叠区间数
