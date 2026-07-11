"""
LeetCode #1870 - Minimum Speed to Arrive on Time
准时到达的列车最小时速
https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/

给你一个浮点数 `hour` ，表示你到达办公室可用的总通勤时间。要到达办公室，你必须按给定次序乘坐 `n` 趟列车。另给你一个长度为 `n` 的整数数组 `dist` ，其中 `dist[i]` 表示第 `i` 趟列车的行驶距离（单位是千米）。
每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。
例如，第 `1` 趟列车需要 `1.5` 小时，那你必须再等待 `0.5` 小时，搭乘在第 2 小时发车的第 `2` 趟列车。
返回能满足你在时限前到达办公室所要求全部列车的 最小正整数 时速（单位：千米每小时），如果无法准时到达，则返回 `-1` 。
生成的测试用例保证答案不超过 `10^7` ，且 `hour` 的 小数点后最多存在两位数字 。

示例 1：
输入：dist = [1,3,2], hour = 6 输出：1 解释：速度为 1 时： - 第 1 趟列车运行需要 1/1 = 1 小时。 - 由于是在整数时间到达，可以立即换乘在第 1 小时发车的列车。第 2 趟列车运行需要 3/1 = 3 小时。 - 由于是在整数时间到达，可以立即换乘在第 4 小时发车的列车。第 3 趟列车运行需要 2/1 = 2 小时。 - 你将会恰好在第 6 小时到达。
示例 2：
输入：dist = [1,3,2], hour = 2.7 输出：3 解释：速度为 3 时： - 第 1 趟列车运行需要 1/3 = 0.33333 小时。 - 由于不是在整数时间到达，故需要等待至第 1 小时才能搭乘列车。第 2 趟列车运行需要 3/3 = 1 小时。 - 由于是在整数时间到达，可以立即换乘在第 2 小时发车的列车。第 3 趟列车运行需要 2/3 = 0.66667 小时。 - 你将会在第 2.66667 小时到达。
示例 3：
输入：dist = [1,3,2], hour = 1.9 输出：-1 解释：不可能准时到达，因为第 3 趟列车最早是在第 2 小时发车。

提示：
`n == dist.length`
`1 <= n <= 10^5`
`1 <= dist[i] <= 10^5`
`1 <= hour <= 10^9`
`hours` 中，小数点后最多存在两位数字
"""

from typing import List, Optional


from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        # If we need at least n hours for n trains (each takes at least 1/n hour for waiting)
        # Minimum possible time with infinite speed: n-1 + epsilon for last train
        # Actually, minimum time = (n-1) * 1/INF + last_dist/INF -> n-1 (waiting) + epsilon
        # More precisely: at infinite speed, first n-1 trains take 0 time but need ceil to next integer
        # So minimum time = n-1 (since each of first n-1 trains requires waiting to next hour)
        # Wait, with infinite speed: train i takes 0 hours, but we must wait to the next integer hour
        # So effectively each train except possibly the last takes at least 1 hour
        # Actually if speed is infinite, distance/speed ≈ 0, but we still need to round up to next integer for all except last
        # So minimum hours = n-1 + (very small for last)
        # If hour <= n-1, impossible (need at least n-1 full hours + some fraction for last)

        if hour <= n - 1:
            return -1

        def can_arrive(speed: int) -> bool:
            total = 0.0
            for i in range(n - 1):
                total += ceil(dist[i] / speed)
            total += dist[-1] / speed
            return total <= hour

        left, right = 1, 10 ** 7
        while left < right:
            mid = (left + right) // 2
            if can_arrive(mid):
                right = mid
            else:
                left = mid + 1

        return left if can_arrive(left) else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 二分查找最小的正整数速度。
# 1. 判断是否可能：最快的速度下，前 n-1 趟列车每趟至少需要 1 小时
#    （因为需要在整点发车，即使运行时间为0也要等待到下一个整点），
#    最后一趟不需要等待。所以 hour 必须 > n-1。
# 2. 对于给定速度 v，计算总时间：前 n-1 趟用 ceil(dist[i]/v)，
#    最后一趟用 dist[n-1]/v。
# 3. 二分查找速度范围 [1, 10^7]。
#
# 时间复杂度: O(n * log(10^7)) = O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 前 n-1 趟需要向上取整（整点发车限制）
# - 最后一趟不需要向上取整（不需要再等下一趟）
# - 速度上界为 10^7（题目保证）
# - 如果 hour <= n-1，无法准时到达
