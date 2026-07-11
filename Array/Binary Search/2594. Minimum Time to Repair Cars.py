"""
LeetCode #2594 - Minimum Time to Repair Cars
修车的最少时间
https://leetcode.cn/problems/minimum-time-to-repair-cars/

给你一个整数数组 `ranks` ，表示一些机械工的 能力值 。`ranks_i` 是第 `i` 位机械工的能力值。能力值为 `r` 的机械工可以在 `r * n^2` 分钟内修好 `n` 辆车。
同时给你一个整数 `cars` ，表示总共需要修理的汽车数目。
请你返回修理所有汽车 最少 需要多少时间。
注意：所有机械工可以同时修理汽车。

示例 1：
输入：ranks = [4,2,3,1], cars = 10 输出：16 解释： - 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。 - 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。 - 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。 - 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。 16 分钟是修理完所有车需要的最少时间。
示例 2：
输入：ranks = [5,1,8], cars = 6 输出：16 解释： - 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。 - 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。 - 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。 16 分钟时修理完所有车需要的最少时间。

提示：
`1 <= ranks.length <= 10^5`
`1 <= ranks[i] <= 100`
`1 <= cars <= 10^6`
"""

from typing import List, Optional


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        import math

        def can(t: int) -> bool:
            total = 0
            for r in ranks:
                total += int(math.isqrt(t // r))
                if total >= cars:
                    return True
            return False

        lo, hi = 1, min(ranks) * cars * cars
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 二分查找最小时间T。检查函数判断在T时间内能否修完所有车：
# 每个能力值为r的机械工最多修sqrt(T/r)辆车（因为r*n^2<=T，n<=sqrt(T/r)）。
# 所有机械工能修的车数之和>=cars则可行。二分上界为min(rank)*cars^2（最慢情况）。
#
# 时间复杂度: O(N log M)，N为机械工数，M为时间上界
# 空间复杂度: O(1)
#
# 关键点:
# - r*n^2<=T → n<=floor(sqrt(T/r))
# - 上界=min(rank)*cars^2（最慢机械工单独修所有车的时间）
# - 使用isqrt精确计算整数平方根
