"""
LeetCode #853 - Car Fleet
中文题名：车队
https://leetcode.com/problems/car-fleet/

`N` cars are going to the same destination along a one lane road.  The
destination is `target` miles away.

Each car `i` has a constant speed `speed[i]` (in miles per
hour), and initial position `position[i]` miles towards the target along the
road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to
bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same
position.

A car fleet is some non-empty set of cars driving at the same position and same
speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered
as one car fleet.

How many car fleets will arrive at the destination?

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

`0 <= N <= 10 ^ 4`

`0 < target <= 10 ^ 6`

`0 < speed[i] <= 10 ^ 6`

`0 <= position[i] < target`

All initial positions are different.

【中文翻译】
有 N 辆车沿着一条单车道驶向同一个目的地。目的地距离 target 英里。

每辆车 i 以恒定的速度 speed[i]（英里/小时）行驶，初始位置 position[i] 英里（沿道路朝向目标）。

一辆车永远不能超过它前面的车，但可以追上前面的车，并以相同的速度紧挨着行驶。两车之间的距离忽略不计——假设它们处于相同的位置。

一个车队是一些在同一位置以相同速度行驶的非空车辆集合。注意单辆车也算一个车队。

如果一辆车恰好在目的地点追上一个车队，它仍然被认为是一个车队。

问有多少个车队会到达目的地？

"""

from typing import List, Optional


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        prev_time = -1.0

        for pos, spd in cars:
            # Time needed to reach target
            time = (target - pos) / spd
            # If this car takes longer than the car ahead, it forms a new fleet
            # (because it cannot catch up)
            if time > prev_time:
                fleets += 1
                prev_time = time
            # Otherwise, it catches up and merges with the fleet ahead

        return fleets



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键洞察：按位置从远到近（离目标从最近到最远）排序车辆。
# 计算每辆车到达目的地所需的时间 time = (target - pos) / speed。
# 从最靠近目的地的车开始遍历：
# 如果当前车的时间 > 前一辆车（更靠近目标的车）的时间，说明它追不上前车，形成新车队。
# 如果当前车的时间 <= 前车的时间，它会追上前车并合并为一个车队（速度变慢）。
# 准确地说，我们维护当前车队的"最慢到达时间"。新来一辆车：
# - 如果它的到达时间更长（更慢），它形成新车队（前面的车队已走，追不上）
# - 如果它的到达时间更短（更快），它会追上前面的车并合并，车队速度由最慢的车决定
#
# 时间复杂度: O(N log N) 排序
# 空间复杂度: O(N) 存储排序后的车辆信息
#
# 关键点:
# - 核心：按初始位置降序排序（离目标近的先处理）
# - 计算到达时间 (target - position) / speed
# - 从后往前遍历：如果后车到达时间长于前车，形成新车队；否则合并
# - 之所以按位置降序是因为后车无法超越前车，前车的速度决定了车队的到达时间
