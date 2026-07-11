"""
LeetCode #1094 - Car Pooling
中文题名：拼车
https://leetcode.com/problems/car-pooling/

You are driving a vehicle that has `capacity` empty seats initially available
for passengers.  The vehicle only drives east (ie. it
cannot turn around and drive west.)

Given a list of `trips`, `trip[i] = [num_passengers, start_location,
end_location]` contains information about the `i`-th trip: the number
of passengers that must be picked up, and the locations to pick them up and drop them off.
The locations are given as the number of kilometers due east from your vehicle's
initial location.

Return `true` if and only if it is possible to pick up and drop off all
passengers for all the given trips.

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

【中文翻译】
假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，车只能向一个方向行驶（即不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份乘客行程计划表 trips[][]，其中 trips[i] = [num_passengers, start_location, end_location] 包含了第 i 组乘客的行程信息：需要接送的乘客数量、乘客的上车地点以及乘客的下车地点。给出的地点是基于车辆的初始位置向东行驶的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则返回 false。

示例 1：

输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

示例 2：

输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true

示例 3：

输入：trips = [[2,1,5],[3,5,7]], capacity = 3
输出：true

示例 4：

输入：trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
输出：true

"""

from typing import List, Optional


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_location = 0
        for _, _, end in trips:
            max_location = max(max_location, end)

        diff = [0] * (max_location + 2)

        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num

        cur = 0
        for i in range(max_location + 1):
            cur += diff[i]
            if cur > capacity:
                return False

        return True










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用差分数组（Difference Array）/ 扫描线算法。
# 将每个行程视为区间 [start, end)，在 start 位置增加 num 人，在 end 位置减少 num 人。
# 1. 找到最大位置 max_location（所有 end 中的最大值）。
# 2. 创建差分数组 diff，长度 max_location + 2。
# 3. 对每个行程：diff[start] += num, diff[end] -= num。
# 4. 遍历所有位置，累加差分值得到当前车上人数 cur。
# 5. 如果任何时刻 cur > capacity，返回 False；否则返回 True。
#
# 时间复杂度: O(n + m) - n 为行程数，m 为最大位置
# 空间复杂度: O(m) - 差分数组大小
#
# 关键点:
# - 差分数组：区间增量操作转化为 O(1) 的两点操作
# - end 位置下车，乘客不计入该位置
# - 前缀和还原每个位置的实时人数
# - 简单高效，无需排序
