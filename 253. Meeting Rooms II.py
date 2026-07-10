"""
LeetCode #253 - Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]`
(s_i < e_i), find the minimum number of conference rooms required.

Example 1:

Input: `[[0, 30],[5, 10],[15, 20]]`
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1

NOTE: input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.
"""

from typing import List, Optional


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 分离开始和结束时间，分别排序
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        rooms = 0
        end_ptr = 0

        for start in start_times:
            # 如果当前开始时间 >= 最早结束时间，说明可以释放一个房间
            if start >= end_times[end_ptr]:
                end_ptr += 1
            else:
                rooms += 1

        return rooms


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 类似"公交车上下客"问题。将所有开始时间和结束时间分别排序。
# 遍历每个开始时间，如果当前开始时间 >= 最早未结束的会议的结束时间，
# 说明该会议已结束，释放房间（end_ptr++）；否则需要新开一个房间。
# 最终 rooms 计数就是所需的最小房间数。
#
# 时间复杂度: O(n log n) — 排序
# 空间复杂度: O(n) — 存储开始和结束时间数组
#
# 关键点：
# - 将时间点分离后排序，无需关注具体是哪个会议
# - start >= end_times[end_ptr] 时复用房间
# - 也可以使用最小堆（优先队列）实现
