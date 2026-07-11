"""
LeetCode #3169 - Count Days Without Meetings
无需开会的工作日
https://leetcode.cn/problems/count-days-without-meetings/

给你一个正整数 `days`，表示员工可工作的总天数（从第 1 天开始）。另给你一个二维数组 `meetings`，长度为 `n`，其中 `meetings[i] = [start_i, end_i]` 表示第 `i` 次会议的开始和结束天数（包含首尾）。
返回员工可工作且没有安排会议的天数。
注意：会议时间可能会有重叠。

示例 1：

输入：days = 10, meetings = [[5,7],[1,3],[9,10]]
输出：2
解释：
第 4 天和第 8 天没有安排会议。
示例 2：

输入：days = 5, meetings = [[2,4],[1,3]]
输出：1
解释：
第 5 天没有安排会议。
示例 3：

输入：days = 6, meetings = [[1,6]]
输出：0
解释：
所有工作日都安排了会议。

提示：
`1 <= days <= 10^9`
`1 <= meetings.length <= 10^5`
`meetings[i].length == 2`
`1 <= meetings[i][0] <= meetings[i][1] <= days`
"""

from typing import List, Optional


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = []
        for start, end in meetings:
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        meeting_days = sum(end - start + 1 for start, end in merged)
        return days - meeting_days



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sorting
#
# 解题思路:
# 会议区间可能重叠，需要先合并。按开始时间排序，然后遍历合并重叠或相邻的区间。
# 合并后计算所有会议覆盖的总天数 = sum(end-start+1)，无会议天数 = 总天数 - 会议天数。
# 区间合并判断：如果新区间起点 > 当前合并区间的终点+1，则不重叠。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)（合并后的区间）
#
# 关键点:
# - 排序后合并重叠区间
# - 相邻区间（前一个end+1==后一个start）也视为连续
# - 总天数 - 会议天数 = 空闲天数
