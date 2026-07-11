"""
LeetCode #1288 - Remove Covered Intervals
中文题名：删除被覆盖区间
https://leetcode.com/problems/remove-covered-intervals/

Given a list of intervals, remove all intervals that are covered by another interval
in the list. Interval `[a,b)` is covered by interval
`[c,d)` if and only if `c <= a` and `b <= d`.

After doing so, return the number of remaining intervals.

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Constraints:

`1 <= intervals.length <= 1000`

`0 <= intervals[i][0] < intervals[i][1] <= 10^5`

`intervals[i] != intervals[j]` for all `i != j`

【中文翻译】
给定一个区间列表，删除所有被列表中其他区间覆盖的区间。区间 [a,b) 被区间 [c,d) 覆盖当且仅当 c <= a 且 b <= d。

完成删除后，返回剩余区间的数量。

示例 1：

输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被 [2,8] 覆盖，因此被删除。

约束条件：

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
对于所有 i != j，intervals[i] != intervals[j]
"""

from typing import List, Optional


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending, then by end descending
        # This way, for intervals with same start, the longer one comes first
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end

        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 将区间按起点升序排序，若起点相同则按终点降序排序。
#    这样处理相同起点的区间时，较长的(终点较大的)排在前面。
# 2. 遍历排序后的区间，维护当前已见过的最大终点 max_end。
# 3. 对于每个区间 [start, end]：
#    - 若 end > max_end，说明该区间没有被任何前面的区间完全覆盖
#      （因为前面的区间起点 <= 当前起点，若终点也更大则覆盖了当前区间）。
#      此时 count++ 并更新 max_end。
#    - 若 end <= max_end，说明该区间被某个前面的区间覆盖，跳过。
# 4. 最后 count 即为未被覆盖的区间数量。
#
# 时间复杂度: O(n log n) - 排序主导
# 空间复杂度: O(1) - 排序原地进行，仅使用常量额外空间（若排序使用额外空间则为 O(log n)）
#
# 关键点:
# - 排序策略：起点升序 + 终点降序，确保相同起点的长区间先处理
# - 只需维护一个 max_end 变量即可判断覆盖关系
# - 区间半开半闭 [a, b)，覆盖条件为 c <= a 且 b <= d
