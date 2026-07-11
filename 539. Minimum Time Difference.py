"""
LeetCode #539 - Minimum Time Difference
中文题名：最小时间差
https://leetcode.com/problems/minimum-time-difference/

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum
minutes difference between any two time points in the list.

Example 1:

Input: ["23:59","00:00"]
Output: 1

Note:

The number of time points in the given list is at least 2 and won't exceed 20000.

The input time is legal and ranges from 00:00 to 23:59.

【中文翻译】
给定一个 24 小时制的时间列表，格式为 "HH:MM"，找出列表中任意两个时间之间的最小分钟差。
时间点数量至少为 2，最多不超过 20000。输入时间合法，范围在 00:00 到 23:59 之间。

示例 1：
    输入：["23:59","00:00"]
    输出：1
    解释：23:59 和 00:00 相差 1 分钟（第二天 00:00 减去前一天 23:59）
"""

from typing import List, Optional


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert each time to total minutes
        minutes = []
        for t in timePoints:
            h, m = t.split(":")
            minutes.append(int(h) * 60 + int(m))

        minutes.sort()

        # Compare adjacent pairs
        min_diff = float("inf")
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Also compare wrap-around: first and last across midnight
        # Smallest time + 1440 minus the largest time
        min_diff = min(min_diff, minutes[0] + 1440 - minutes[-1])

        return min_diff



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 先将每个时间点转换为从 00:00 开始的总分钟数（小时×60 + 分钟），然后对所有分钟数排序。
# 排序后，相邻两个时间点的差值构成了候选的最小差。此外还需处理跨天的情况：
# 将最小时间加上 1440（一天的分钟数）减去最大时间，即首尾差值（相当于第二天的最早时间与前一天最晚时间的差）。
# 取所有差值的最小值返回。
#
# 时间复杂度: O(N log N) — 排序的时间开销
# 空间复杂度: O(N) — 存储所有时间转换后的分钟数组
#
# 关键点:
# - 统一转换为分钟数简化比较：HH*60 + MM
# - 排序后只需比较相邻元素（排序数组中最小差一定出现在相邻元素之间）
# - 必须处理跨天情况：最晚时间和最早时间（+ 1440）的差值
# - 鸽巢原理优化：若 N > 1440，一定存在重复时间，可直接返回 0
