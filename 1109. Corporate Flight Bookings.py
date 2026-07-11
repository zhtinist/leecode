"""
LeetCode #1109 - Corporate Flight Bookings
中文题名：航班预订统计
https://leetcode.com/problems/corporate-flight-bookings/

There are `n` flights, and they are labeled from `1` to
`n`.

We have a list of flight bookings.  The `i`-th booking `bookings[i]
= [i, j, k]` means that we booked `k` seats from flights labeled
`i` to `j` inclusive.

Return an array `answer` of length `n`, representing the number of
seats booked on each flight in order of their label.

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]

Constraints:

`1 <= bookings.length <= 20000`

`1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000`

`1 <= bookings[i][2] <= 10000`

【中文翻译】
这里有 n 个航班，它们分别从 1 到 n 进行编号。

我们有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。

返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。

示例 1：

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]

约束条件：

`1 <= bookings.length <= 20000`

`1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000`

`1 <= bookings[i][2] <= 10000`
"""

from typing import List, Optional


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)
        for i, j, k in bookings:
            diff[i] += k
            diff[j + 1] -= k

        result = [0] * n
        cur = 0
        for i in range(1, n + 1):
            cur += diff[i]
            result[i - 1] = cur

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用差分数组（Difference Array）技巧。差分数组的核心思想是：对于区间 [i, j] 上的统一增量 k，
# 只需要在 diff[i] += k，diff[j+1] -= k，然后通过前缀和恢复出每个位置的最终值。
# 1. 创建大小为 n+2 的差分数组 diff（多一个位置处理 j+1 越界）。
# 2. 遍历每条预订记录 [i, j, k]：diff[i] += k, diff[j+1] -= k。
# 3. 对差分数组求前缀和，第 i 个位置的前缀和即为航班 i 的预订座位总数。
#
# 时间复杂度: O(n + m) - n 为航班数，m 为预订记录数
# 空间复杂度: O(n) - 差分数组与结果数组
#
# 关键点:
# - 差分数组是处理区间增减问题的经典技巧，将 O(n*m) 的暴力更新优化为 O(n+m)
# - 差分数组比原数组多开一位，方便处理 j+1 越界的情况
