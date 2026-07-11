"""
LeetCode #1654 - Minimum Jumps to Reach Home
中文题名：到家的最少跳跃次数
https://leetcode.com/problems/minimum-jumps-to-reach-home/

A certain bug's home is on the x-axis at position `x`. Help them get
there from position `0`.

The bug jumps according to the following rules:

It can jump exactly `a` positions forward (to the
right).

It can jump exactly `b` positions backward (to the
left).

It cannot jump backward twice in a row.

It cannot jump to any `forbidden` positions.

The bug may jump forward beyond its home, but it cannot
jump to positions numbered with negative integers.

Given an array of integers `forbidden`, where `forbidden[i]`
means that the bug cannot jump to the position `forbidden[i]`, and
integers `a`, `b`, and `x`, return the minimum
number of jumps needed for the bug to reach its home. If there is no
possible sequence of jumps that lands the bug on position `x`, return
`-1.`

Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.

Example 2:

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1

Example 3:

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.

Constraints:

`1 <= forbidden.length <= 1000`

`1 <= a, b, forbidden[i] <= 2000`

`0 <= x <= 2000`

All the elements in `forbidden` are distinct.

Position `x` is not forbidden.

【中文翻译】
一只跳蚤在 x 轴上跳跃，从位置 0 开始。每次可以向前跳 a 个单位或向后跳 b 个单位。
但不能跳到 forbidden 数组中的任何位置，也不能连续两次向后跳。求到达位置 x 的最少跳跃次数。
如果无法到达，返回 -1。

示例 1：
输入: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
输出: 3
解释: 0→3(前)→6(前)→9(前) 共3步。
"""

from typing import List, Optional
from collections import deque


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        limit = max(x, max(forbidden)) + a + b

        queue = deque([(0, 0)])
        visited = {(0, 0)}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                pos, is_back = queue.popleft()
                if pos == x:
                    return steps

                next_pos = pos + a
                if next_pos <= limit and next_pos not in forbidden_set and (next_pos, 0) not in visited:
                    visited.add((next_pos, 0))
                    queue.append((next_pos, 0))

                if is_back == 0:
                    next_pos = pos - b
                    if next_pos >= 0 and next_pos not in forbidden_set and (next_pos, 1) not in visited:
                        visited.add((next_pos, 1))
                        queue.append((next_pos, 1))

            steps += 1

        return -1
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# BFS 搜索。状态为 (position, is_backward) 其中 is_backward 表示上一步是否向后跳。
# - 向前跳：永远允许，需检查不超过上界
# - 向后跳：仅当上一步不是向后跳时才允许，不能跳到负数位置
# 上界设置为 max(x, max(forbidden)) + a + b（安全上界）。
# visited 集合跟踪 (pos, is_back) 状态。
#
# 时间复杂度: O(Limit) — BFS 搜索范围有限
# 空间复杂度: O(Limit) — 队列和 visited 集合
#
# 关键点:
# - 状态包含是否连续后退的信息（因为不能连续后退）
# - 上界不必无限大，max(x, max(forbidden)) + a + b 足够
