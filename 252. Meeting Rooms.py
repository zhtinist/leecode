"""
LeetCode #252 - Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]`
(s_i < e_i), determine if a person could attend all meetings.

Example 1:

Input: `[[0,30],[5,10],[15,20]]`
Output: false

Example 2:

Input: [[7,10],[2,4]]
Output: true

NOTE: input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.
"""

from typing import List, Optional


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])

        # 检查相邻会议是否重叠
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: Yes
#
# 解题思路：
# 按会议开始时间排序，然后检查相邻会议是否重叠。如果前一个会议的结束时间
# 大于后一个会议的开始时间，则存在重叠，无法参加所有会议。
#
# 时间复杂度: O(n log n) — 排序
# 空间复杂度: O(1) 或 O(n) — 取决于排序算法
#
# 关键点：
# - 按开始时间排序后，只需检查相邻会议
# - 重叠条件: intervals[i][0] < intervals[i-1][1]
