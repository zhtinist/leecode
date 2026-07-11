"""
LeetCode #2187 - Minimum Time to Complete Trips
完成旅途的最少时间
https://leetcode.cn/problems/minimum-time-to-complete-trips/

给你一个数组 `time` ，其中 `time[i]` 表示第 `i` 辆公交车完成 一趟旅途 所需要花费的时间。
每辆公交车可以 连续 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 立马开始 下一趟旅途。每辆公交车 独立 运行，也就是说可以同时有多辆公交车在运行且互不影响。
给你一个整数 `totalTrips` ，表示所有公交车 总共 需要完成的旅途数目。请你返回完成 至少 `totalTrips` 趟旅途需要花费的 最少 时间。

示例 1：
输入：time = [1,2,3], totalTrips = 5 输出：3 解释： - 时刻 t = 1 ，每辆公交车完成的旅途数分别为 [1,0,0] 。   已完成的总旅途数为 1 + 0 + 0 = 1 。 - 时刻 t = 2 ，每辆公交车完成的旅途数分别为 [2,1,0] 。   已完成的总旅途数为 2 + 1 + 0 = 3 。 - 时刻 t = 3 ，每辆公交车完成的旅途数分别为 [3,1,1] 。   已完成的总旅途数为 3 + 1 + 1 = 5 。 所以总共完成至少 5 趟旅途的最少时间为 3 。
示例 2：
输入：time = [2], totalTrips = 1 输出：2 解释： 只有一辆公交车，它将在时刻 t = 2 完成第一趟旅途。 所以完成 1 趟旅途的最少时间为 2 。

提示：
`1 <= time.length <= 10^5`
`1 <= time[i], totalTrips <= 10^7`
"""

from typing import List, Optional


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        二分答案：在 [1, min(time) * totalTrips] 范围内二分搜索最小时间 T，
        使得所有公交车在时间 T 内完成的总趟数 >= totalTrips。
        """
        left = 1
        right = min(time) * totalTrips  # 上界：最快公交车独自完成所有趟数的时间

        while left < right:
            mid = (left + right) // 2
            # 计算在时间 mid 内所有公交车能完成的总趟数
            trips = sum(mid // t for t in time)
            if trips >= totalTrips:
                right = mid   # 尝试更小的答案
            else:
                left = mid + 1  # 需要更多时间

        return left


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 1. 答案具有单调性：如果时间 T 能完成 totalTrips 趟，那么 T+1 也一定能。
#    因此可以使用二分查找。
# 2. 搜索范围：
#    - 下界 left = 1（至少需要 1 单位时间）
#    - 上界 right = min(time) * totalTrips（最快公交独干的最坏情况）
# 3. 对于每个中间值 mid，计算 sum(mid // time[i])，
#    即所有公交在 mid 时间内各自能完成的总趟数之和。
# 4. 如果总趟数 >= totalTrips，尝试更小的时间 right = mid；
#    否则需要更多时间 left = mid + 1。
# 5. 当 left == right 时找到最小时间。
#
# 时间复杂度: O(n * log(min(time) * totalTrips))
# - n 为公交车数量，每次二分需要 O(n) 计算总趟数。
# - 二分次数约为 log(min(time) * totalTrips)，上限约 60。
#
# 空间复杂度: O(1)
# - 只使用常数额外空间。
#
# 关键点:
# - 最小时间由最快的公交车决定上界。
# - sum(mid // t) 可能很大，注意使用 Python 的大整数。
# - 二分模板使用 while left < right 模式，返回 left。
