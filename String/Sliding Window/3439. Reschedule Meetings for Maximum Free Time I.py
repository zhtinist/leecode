"""
LeetCode #3439 - Reschedule Meetings for Maximum Free Time I
重新安排会议得到最多空余时间 I
https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/

给你一个整数 `eventTime` 表示一个活动的总时长，这个活动开始于 `t = 0` ，结束于 `t = eventTime` 。
同时给你两个长度为 `n` 的整数数组 `startTime` 和 `endTime` 。它们表示这次活动中 `n` 个时间 没有重叠 的会议，其中第 `i` 个会议的时间为 `[startTime[i], endTime[i]]` 。
你可以重新安排 至多 `k` 个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 相邻两个会议之间的 最长 连续空余时间。
移动前后所有会议之间的 相对 顺序需要保持不变，而且会议时间也需要保持互不重叠。
请你返回重新安排会议以后，可以得到的 最大 空余时间。
注意，会议 不能 安排到整个活动的时间以外。

示例 1：

输入：eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
输出：2
解释：

将 `[1, 2]` 的会议安排到 `[2, 3]` ，得到空余时间 `[0, 2]` 。
示例 2：

输入：eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]
输出：6
解释：

将 `[2, 4]` 的会议安排到 `[1, 3]` ，得到空余时间 `[3, 9]` 。
示例 3：

输入：eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
输出：0
解释：
活动中的所有时间都被会议安排满了。

提示：
`1 <= eventTime <= 10^9`
`n == startTime.length == endTime.length`
`2 <= n <= 10^5`
`1 <= k <= n`
`0 <= startTime[i] < endTime[i] <= eventTime`
`endTime[i] <= startTime[i + 1]` 其中 `i` 在范围 `[0, n - 2]` 之间。
"""

from typing import List, Optional


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        # Compute gaps: before first meeting, between meetings, after last meeting
        gaps = []
        gaps.append(startTime[0] - 0)
        for i in range(n - 1):
            gaps.append(startTime[i + 1] - endTime[i])
        gaps.append(eventTime - endTime[-1])

        # We have n+1 gaps. We can move at most k meetings.
        # Moving k meetings can merge up to k+1 consecutive gaps.
        # Find max sum of k+1 consecutive gaps.
        window = k + 1
        cur = sum(gaps[:window])
        ans = cur
        for i in range(window, len(gaps)):
            cur += gaps[i] - gaps[i - window]
            ans = max(ans, cur)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sliding Window
#
# 解题思路:
# 1. 计算相邻会议之间的空余时间 gaps（包括开头到第一个会议、最后一个会议到结尾）
# 2. 移动 k 个会议可以使 k+1 个连续的空余时间合并成一个大的空余时间块
#    - 因为我们可以把中间的 k 个会议移到这 k+1 个间隙的任意位置
# 3. 问题转化为：在 gaps 数组中找长度为 k+1 的最大滑动窗口和
# 4. 返回最大窗口和
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 会议相对顺序不变，所以移动会议只能把连续的间隙合并
# - gaps 有 n+1 个（n 个会议之间有 n+1 个空隙）
# - 移动 k 个会议可以消除 k 个间隔，留下 k+1 个间隙的总和
