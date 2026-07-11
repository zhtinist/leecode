"""
LeetCode #436 - Find Right Interval
中文题名：寻找右区间
https://leetcode.com/problems/find-right-interval/

Given a set of intervals, for each of the interval i, check if there exists an interval j
whose start point is bigger than or equal to the end point of the interval i, which can be
called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that
the interval j has the minimum start point to build the "right" relationship for
interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you
need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.

You may assume none of these intervals have the same start point.

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

NOTE: input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.

【中文翻译】
给定一组区间，对于每个区间 i，检查是否存在另一个区间 j，其起点大于或等于区间 i 的终点，
这被称为 j 在 i 的"右侧"。对于任何区间 i，需要存储区间 j 的最小索引，
即区间 j 具有最小的起点来建立与 i 的"右侧"关系。如果 j 不存在，则为区间 i 存储 -1。
最后需要将每个区间存储的值作为数组输出。

注意：
    区间终点始终大于起点。
    所有区间的起点互不相同。

示例 1：输入 [[1,2]] → 输出 [-1]
示例 2：输入 [[3,4],[2,3],[1,2]] → 输出 [-1,0,1]
    [3,4] 没有"右"区间；[2,3] 的右区间是 [3,4]（索引 0）；[1,2] 的右区间是 [2,3]（索引 1）
示例 3：输入 [[1,4],[2,3],[3,4]] → 输出 [-1,2,-1]
    [1,4] 和 [3,4] 没有右区间；[2,3] 的右区间是 [3,4]（索引 2）
"""

from typing import List, Optional
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Pair start with original index
        starts = [(intervals[i][0], i) for i in range(n)]
        starts.sort()  # Sort by start value

        result = [-1] * n

        for i in range(n):
            end = intervals[i][1]
            # Binary search for the smallest start >= end
            idx = bisect.bisect_left(starts, (end, -1))
            if idx < n:
                result[i] = starts[idx][1]  # Original index

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二分查找。对于每个区间，需要找到起点 >= 其终点的最小区间（按起点最小），并返回其原始索引。
#
# 1. 提取所有区间的起点并与原始索引配对：starts = [(start, original_index), ...]
# 2. 按起点升序排序 starts 列表
# 3. 对于每个区间，用二分查找在 starts 中找第一个起点 >= 当前终点 end 的位置
# 4. 如果找到（idx < n），将对应原始索引存入结果；否则为 -1
#
# 使用 bisect_left 实现二分查找。将 (end, -1) 作为查找目标，-1 确保当起点等于 end 时
# 能找到该位置（因为起点互不相同）。
#
# 时间复杂度: O(N log N) — 排序 O(N log N) + 每个区间二分查找 O(log N)
# 空间复杂度: O(N) — starts 数组
#
# 关键点:
# - 提取起点并保留原始索引是核心技巧
# - bisect_left 找第一个 >= 目标的位置
# - 按起点排序后二分查找
