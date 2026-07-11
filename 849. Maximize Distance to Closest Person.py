"""
LeetCode #849 - Maximize Distance to Closest Person
中文题名：到最近的人的最大距离
https://leetcode.com/problems/maximize-distance-to-closest-person/

In a row of `seats`, `1` represents a person sitting in that seat, and
`0` represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to
him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Note:

`1 <= seats.length <= 20000`

`seats` contains only 0s or 1s, at least one `0`, and
at
least one `1`.

【中文翻译】
在一排座位 `seats` 中，`1` 表示该座位上有人，`0` 表示该座位为空。

至少有一个空座位，且至少有一个人。

亚历克斯想坐在一个座位上，使得他与最近的人之间的距离最大化。

返回他到最近的人的最大距离。

示例 1：

输入：[1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空座位（seats[2]），则最近的人距离为 2。
如果亚历克斯坐在其他任何空座位，最近的人距离为 1。
因此，到最近的人的最大距离为 2。

示例 2：

输入：[1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位，最近的人距离为 3。
这是可能的最大距离，所以答案是 3。

注意：

`1 <= seats.length <= 20000`

`seats` 只包含 0 或 1，至少有一个 `0`，且至少有一个 `1`。

"""

from typing import List, Optional


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_dist = 0

        # Find the distance from the left edge to the first person
        first_person = 0
        while seats[first_person] == 0:
            first_person += 1
        max_dist = first_person  # Distance if sitting at the leftmost seat

        # Find max gap between two people
        prev = first_person
        for i in range(prev + 1, n):
            if seats[i] == 1:
                # Distance is half the gap (sit in the middle)
                gap = i - prev
                max_dist = max(max_dist, gap // 2)
                prev = i

        # Find the distance from the last person to the right edge
        last_person = prev
        right_dist = n - 1 - last_person
        max_dist = max(max_dist, right_dist)

        return max_dist



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 一次遍历，考虑三种情况。
# 1. 左边缘到第一个人的距离：坐在最左端时的距离 = first_person 的下标
# 2. 两个相邻的人之间的最大距离：坐在中间时，离最近的人的距离为 gap // 2
# 3. 最后一个人到右边缘的距离：坐在最右端时的距离 = n - 1 - last_person 的下标
# 取三种情况的最大值。
#
# 时间复杂度: O(n) — 一次线性遍历
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - 三种情况：左边缘、两个1之间、右边缘
# - 两个1之间时，坐在正中间可最大化最小距离
# - 边缘处可以直接坐到最边上，不需要除以 2
# - 至少有一个空位和一个人，边界条件安全
