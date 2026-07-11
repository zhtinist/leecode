"""
LeetCode #3440 - Reschedule Meetings for Maximum Free Time II
重新安排会议得到最多空余时间 II
https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/

给你一个整数 `eventTime` 表示一个活动的总时长，这个活动开始于 `t = 0` ，结束于 `t = eventTime` 。
同时给你两个长度为 `n` 的整数数组 `startTime` 和 `endTime` 。它们表示这次活动中 `n` 个时间 没有重叠 的会议，其中第 `i` 个会议的时间为 `[startTime[i], endTime[i]]` 。
你可以重新安排 至多 一个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 最长 连续空余时间。
请你返回重新安排会议以后，可以得到的 最大 空余时间。
注意，会议 不能 安排到整个活动的时间以外，且会议之间需要保持互不重叠。
注意：重新安排会议以后，会议之间的顺序可以发生改变。

示例 1：

输入：eventTime = 5, startTime = [1,3], endTime = [2,5]
输出：2
解释：

将 `[1, 2]` 的会议安排到 `[2, 3]` ，得到空余时间 `[0, 2]` 。
示例 2：

输入：eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]
输出：7
解释：

将 `[0, 1]` 的会议安排到 `[8, 9]` ，得到空余时间 `[0, 7]` 。
示例 3：

输入：eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]
输出：6
解释：

将 `[3, 4]` 的会议安排到 `[8, 9]` ，得到空余时间 `[1, 7]` 。
示例 4：

输入：eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
输出：0
解释：
活动中的所有时间都被会议安排满了。

提示：
`1 <= eventTime <= 10^9`
`n == startTime.length == endTime.length`
`2 <= n <= 10^5`
`0 <= startTime[i] < endTime[i] <= eventTime`
`endTime[i] <= startTime[i + 1]` 其中 `i` 在范围 `[0, n - 2]` 之间。
"""

from typing import List, Optional


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        # Compute gaps between meetings
        gaps = [startTime[0]]
        for i in range(n - 1):
            gaps.append(startTime[i + 1] - endTime[i])
        gaps.append(eventTime - endTime[-1])

        m = len(gaps)  # n + 1

        # Prefix max and suffix max for O(1) "max excluding i, i+1"
        pref_max = [0] * m
        for i in range(m):
            pref_max[i] = gaps[i]
            if i > 0:
                pref_max[i] = max(pref_max[i], pref_max[i - 1])

        suff_max = [0] * m
        for i in range(m - 1, -1, -1):
            suff_max[i] = gaps[i]
            if i < m - 1:
                suff_max[i] = max(suff_max[i], suff_max[i + 1])

        ans = max(gaps)  # Option: don't move any meeting

        for i in range(n):
            dur = endTime[i] - startTime[i]
            left_gap = gaps[i]
            right_gap = gaps[i + 1]
            merged = left_gap + dur + right_gap

            # Best gap NOT adjacent to meeting i
            best_other = 0
            if i > 0:
                best_other = max(best_other, pref_max[i - 1])
            if i + 2 < m:
                best_other = max(best_other, suff_max[i + 2])

            if best_other >= dur:
                # Can place meeting in another gap, full merged space is free
                ans = max(ans, merged)
            else:
                # Place meeting at one end of merged space
                ans = max(ans, left_gap + right_gap)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Enumeration
#
# 解题思路:
# 1. 计算所有会议空隙 gaps（共 n+1 个）
# 2. 枚举每个会议 i 作为要移动的目标：
#    - 移除会议 i 会将 gaps[i] + duration[i] + gaps[i+1] 合并为连续空闲时间
#    - 需要将会议 i 放置到其他位置（需要某个空隙 >= duration[i]）
# 3. 使用前后缀最大值快速查询"除 i 和 i+1 外的最大空隙"
# 4. 若存在其他空隙能容纳该会议，答案为 merged
#    否则将该会议放在合并空隙的一端，答案为 gaps[i] + gaps[i+1]
# 5. 同时考虑不移动任何会议的基准情况
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 会议顺序可变，所以可以移动到任意空隙
# - 移除会议将两侧空隙合并
# - 前后缀最大值用于 O(1) 查询排除特定位置的全局最大值
