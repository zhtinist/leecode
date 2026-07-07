"""
LeetCode #57 - Insert Interval
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where
intervals[i] = [start_i, end_i] represent the start and the end of the ith
interval and intervals is sorted in ascending order by start_i. You are also
given an interval newInterval = [start, end] that represents the start and end
of another interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by start_i and intervals still does not have any overlapping
intervals (merge intervals if necessary).

Return intervals after the insertion.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= start_i <= end_i <= 10^5
    intervals is sorted by start_i in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 10^5
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        start, end = newInterval

        # 第一段：新区间左边的区间，完全在 newInterval 之前，不会重叠
        # 条件：当前区间右端点 < 新区间左端点
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 第二段：与新区间重叠的区间，全部合并进 newInterval
        # 重叠条件：当前区间左端点 <= 已合并区间的右端点
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])   # 合并后取最小左端点
            end = max(end, intervals[i][1])       # 合并后取最大右端点
            i += 1
        result.append([start, end])

        # 第三段：新区间右边的区间，完全在 newInterval 之后
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
