"""
LeetCode #2332 - The Latest Time to Catch a Bus
坐上公交的最晚时间
https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/

给你一个下标从 0 开始长度为 `n` 的整数数组 `buses` ，其中 `buses[i]` 表示第 `i` 辆公交车的出发时间。同时给你一个下标从 0 开始长度为 `m` 的整数数组 `passengers` ，其中 `passengers[j]` 表示第 `j` 位乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。
给你一个整数 `capacity` ，表示每辆公交车 最多 能容纳的乘客数目。
每位乘客都会排队搭乘下一辆有座位的公交车。如果你在 `y` 时刻到达，公交在 `x` 时刻出发，满足 `y <= x`  且公交没有满，那么你可以搭乘这一辆公交。最早 到达的乘客优先上车。
返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。
注意：数组 `buses` 和 `passengers` 不一定是有序的。

示例 1：
输入：buses = [10,20], passengers = [2,17,18,19], capacity = 2 输出：16 解释： 第 1 辆公交车载着第 1 位乘客。 第 2 辆公交车载着你和第 2 位乘客。 注意你不能跟其他乘客同一时间到达，所以你必须在第二位乘客之前到达。
示例 2：
输入：buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2 输出：20 解释： 第 1 辆公交车载着第 4 位乘客。 第 2 辆公交车载着第 6 位和第 2 位乘客。 第 3 辆公交车载着第 1 位乘客和你。

提示：
`n == buses.length`
`m == passengers.length`
`1 <= n, m, capacity <= 10^5`
`2 <= buses[i], passengers[i] <= 10^9`
`buses` 中的元素 互不相同 。
`passengers` 中的元素 互不相同 。
"""

from typing import List, Optional


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        """
        Sort buses and passengers. Simulate boarding with two pointers.
        After all buses depart, determine the latest possible arrival time:
        - If the last bus has remaining capacity, try arriving at its departure time.
        - Otherwise, try arriving just before the last passenger who boarded.
        Decrement until we find a time not occupied by any passenger.
        """
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)

        j = 0  # index of next passenger to board
        cnt = 0  # passengers on current bus

        for bus_time in buses:
            cnt = 0
            while j < len(passengers) and passengers[j] <= bus_time and cnt < capacity:
                j += 1
                cnt += 1

        # After simulation: j = total passengers who boarded
        # cnt = number on the last bus
        if cnt < capacity:
            ans = buses[-1]
        else:
            ans = passengers[j - 1] - 1

        # Ensure the time is not already taken by another passenger
        while ans in passenger_set:
            ans -= 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Binary Search, Sorting
#
# 解题思路:
# 1. 对公交车出发时间和乘客到达时间分别排序。
# 2. 使用双指针模拟上车过程：对于每辆公交车，按到达顺序装载最多 capacity 名
#    到达时间不晚于出发时间的乘客。
# 3. 模拟完成后确定最晚到达时间：
#    - 若最后一辆公交车未满员，可以尝试在公交车出发时刻到达
#    - 若已满员，尝试在最后一位上车的乘客到达时间之前一秒到达
# 4. 如果该时间已被其他乘客占用，则向前递减直到找到未被占用的时间。
#
# 时间复杂度: O(n log n + m log m) — 排序占主导，双指针模拟为 O(n + m)
# 空间复杂度: O(m) — 存储乘客到达时间的哈希集合用于快速冲突检测
#
# 关键点:
# - 排序是必须的，因为最早到达的乘客优先上车
# - 最后上车的乘客索引为 j-1，其到达时间 -1 是一个候选解
# - 必须检查候选时间是否与其他乘客冲突
# - 可以通过在最后一辆公交车的出发时刻到达（若未满员）获得更晚的时间
