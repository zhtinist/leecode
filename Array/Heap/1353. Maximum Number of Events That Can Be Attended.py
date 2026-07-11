"""
LeetCode #1353 - Maximum Number of Events That Can Be Attended
中文题名：最多可以参加的会议数目
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

Given an array of `events` where `events[i] = [startDayi,
endDayi]`. Every event `i` starts
at `startDayi` and ends
at `endDayi`.

You can attend an event `i` at any day `d` where `startTimei <=
d <= endTimei`. Notice that you can only attend one event at any
time `d`.

Return the maximum number of events you can attend.

Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

Example 4:

Input: events = [[1,100000]]
Output: 1

Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7

Constraints:

`1 <= events.length <= 10^5`

`events[i].length == 2`

`1 <= events[i][0] <= events[i][1] <= 10^5`

【中文翻译】
给定一个 `events` 数组，其中 `events[i] = [startDayi, endDayi]`，表示第 `i` 个会议从 `startDayi` 开始到 `endDayi` 结束。

你可以参加任意一天 `d` 的某个会议，其中 `startTimei <= d <= endTimei`。注意你每天只能参加一个会议。

返回最多可以参加的会议数目。

示例 1：
输入：events = [[1,2],[2,3],[3,4]]
输出：3
解释：你可以参加所有三个会议。
安排会议的一种方式如上图。
第 1 天参加第一个会议。
第 2 天参加第二个会议。
第 3 天参加第三个会议。

示例 2：
输入：events = [[1,2],[2,3],[3,4],[1,2]]
输出：4

示例 3：
输入：events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
输出：4

示例 4：
输入：events = [[1,100000]]
输出：1

示例 5：
输入：events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
输出：7
"""

from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        max_day = max(end for _, end in events)
        heap = []
        event_idx = 0
        attended = 0

        for day in range(1, max_day + 1):
            # 将所有从今天开始的会议加入堆中（按结束时间排序）
            while event_idx < len(events) and events[event_idx][0] == day:
                heapq.heappush(heap, events[event_idx][1])
                event_idx += 1

            # 移除已经过期的会议
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # 参加结束时间最早的会议
            if heap:
                heapq.heappop(heap)
                attended += 1

        return attended



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：每一天都尽量参加结束时间最早的会议，为后续天数留出更多选择空间。
# 1. 按开始时间对会议排序。
# 2. 从第 1 天遍历到最后一天（max_day）：
#    a. 将当天开始的所有会议的结束时间加入最小堆。
#    b. 从堆中弹出所有已经过期（结束时间 < 当天）的会议。
#    c. 如果堆非空，参加结束时间最早的会议（弹出堆顶），计数加 1。
# 3. 返回参加的总数。
#
# 时间复杂度: O(N log N)，N 为会议数量（排序 O(N log N)，堆操作 O(N log N)）
# 空间复杂度: O(N)，堆最多存储 N 个会议
#
# 关键点:
# - 贪心选择：每天参加结束时间最早的会议
# - 按开始时间排序，逐天处理
# - 用最小堆维护可选择会议的结束时间
# - 及时清理已过期会议避免无效遍历













