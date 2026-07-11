"""
LeetCode #1386 - Cinema Seat Allocation
中文题名：安排电影院座位
https://leetcode.com/problems/cinema-seat-allocation/

A cinema has `n` rows of seats, numbered from 1 to
`n` and there are ten seats in each row, labelled from 1 to
10 as shown in the figure above.

Given the array `reservedSeats` containing the numbers of seats already
reserved, for example, `reservedSeats[i]=[3,8]` means the seat
located in row 3 and labelled with 8 is already
reserved.

Return the maximum number of four-person families you can allocate on the cinema seats.
A four-person family occupies fours seats in one row, that are
next to each other. Seats across an aisle (such as [3,3] and
[3,4]) are not considered to be next to each other, however, It is permissible for
the four-person family to be separated by an aisle, but in that case, exactly
two people have to sit on each side of the aisle.

Example 1:

Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four families, where seats mark with blue are already reserved and contiguous seats mark with orange are for one family.

Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2

Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4

Constraints:

`1 <= n <= 10^9`

`1 <= reservedSeats.length <= min(10*n, 10^4)`

`reservedSeats[i].length == 2`

`1 <= reservedSeats[i][0] <= n`

`1 <= reservedSeats[i][1] <= 10`

All `reservedSeats[i]` are distinct.

【中文翻译】

电影院有 n 排座位，编号从 1 到 n，每排有十个座位，标号从 1 到 10。

给定数组 reservedSeats，包含已预订座位的编号，例如 reservedSeats[i]=[3,8] 表示第 3 排第 8 座已被预订。

返回最多可以安排多少个四人家庭。四人家庭需要同一排中四个相邻的座位。过道两侧的座位（如 [3,3] 和 [3,4]）不算相邻，但允许家庭被过道分开——此时每侧必须恰好坐两人。

示例 1：
输入：n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
输出：4
解释：上图展示了四个家庭的最佳安排。

示例 2：
输入：n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
输出：2

示例 3：
输入：n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
输出：4

约束条件：
1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
所有 reservedSeats[i] 互不相同。
"""

from typing import List, Optional


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # 用字典存储每行的位掩码（只存有预订的行）
        row_mask = {}
        for row, seat in reservedSeats:
            if row not in row_mask:
                row_mask[row] = 0
            # 只标记座位 2-9（座位 1 和 10 不影响四人家庭）
            if 2 <= seat <= 9:
                row_mask[row] |= (1 << (seat - 2))

        # 没有预订的行，每行最多安排 2 个家庭
        total = 2 * (n - len(row_mask))

        # 左块掩码：座位 2,3,4,5（二进制位 0-3）
        left_mask = 0b1111  # bits 0-3
        # 右块掩码：座位 6,7,8,9（二进制位 4-7）
        right_mask = 0b11110000  # bits 4-7
        # 中间块掩码：座位 4,5,6,7（二进制位 2-5）
        mid_mask = 0b00111100  # bits 2-5

        for mask in row_mask.values():
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            mid_free = (mask & mid_mask) == 0

            if left_free and right_free:
                total += 2
            elif left_free or right_free or mid_free:
                total += 1

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用位掩码（bitmask）表示每行哪些座位已被预订。
# 四人家庭可以安排的位置只有三种：
#   左块：座位 2-5（过道左侧两个 + 过道右侧两个）
#   右块：座位 6-9
#   中间块：座位 4-7（跨过道，每侧两人）
# 对于每行有预订的行，检查三种块是否可用。
# 没有预订的行最多可安排 2 个家庭。
#
# 时间复杂度: O(R)  R 为已被预订的座位数
# 空间复杂度: O(R)  字典存储已被预订的行
#
# 关键点:
# - n 最大可达 10^9，不能遍历所有行，只能处理有预订的行
# - 座位 1 和 10 不影响四人家庭安排，可以忽略
# - 用位掩码高效判断块是否空闲
# - 三种可能的四人家庭位置：左块(2-5)、右块(6-9)、中间块(4-7)










