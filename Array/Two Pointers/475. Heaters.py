"""
LeetCode #475 - Heaters
中文题名：供暖器
https://leetcode.com/problems/heaters/

Winter is coming! Your first job during the contest is to design a standard heater with fixed
warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum
radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected
output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed
25000.

Positions of houses and heaters you are given are non-negative and will not exceed
10^9.

As long as a house is in the heaters' warm radius range, it can be warmed.

All the heaters follow your radius standard and the warm radius will the same.

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

【中文翻译】
冬天来了！你的第一项任务是设计一个具有固定加热半径的供暖器来加热所有房屋。

现在，给定水平线上房屋和供暖器的位置，找出供暖器的最小半径，使得所有房屋都能被供暖器覆盖。

注意：
    房屋和供暖器的数量均为非负整数，且不超过 25000。
    房屋和供暖器的位置均为非负整数，且不超过 10^9。
    只要房屋位于供暖器的加热半径范围内，就能被加热。
    所有供暖器的加热半径相同。

示例 1：
    输入：[1,2,3],[2]
    输出：1
    解释：唯一一个供暖器位于位置 2，如果使用半径 1，则所有房屋都能被加热。

示例 2：
    输入：[1,2,3,4],[1,4]
    输出：1
    解释：两个供暖器分别位于位置 1 和 4。需要使用半径 1，这样所有房屋都能被加热。
"""

from typing import List, Optional
import bisect


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def nearest_heater_dist(house: int) -> int:
            """Return distance from house to the nearest heater."""
            idx = bisect.bisect_left(heaters, house)

            # Closest heater is either heaters[idx] or heaters[idx-1]
            left_dist = house - heaters[idx - 1] if idx > 0 else float("inf")
            right_dist = heaters[idx] - house if idx < len(heaters) else float("inf")
            return min(left_dist, right_dist)

        # The answer is the maximum of the minimum distances for each house
        return max(nearest_heater_dist(h) for h in houses)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 对供暖器数组排序后，对于每个房屋使用二分查找找到其左右最近的供暖器，计算最小距离。
# 所有房屋中最大的那个最小距离，就是需要的最小供暖半径。核心思想：要覆盖最远的那个房屋，
# 半径必须至少等于它到最近供暖器的距离，而这个半径自然也能覆盖所有其他房屋。
#
# 时间复杂度: O(N log M + M log M)，其中 N 是房屋数，M 是供暖器数。
#             排序供暖器 O(M log M)，每个房屋二分查找 O(log M)
# 空间复杂度: O(1) — 仅使用常数额外空间（不计算排序所需栈空间）
#
# 关键点:
# - 排序供暖器后二分查找每个房屋的最近供暖器
# - 最终答案是 max(min_dist)，即所有"房屋到最近供暖器距离"中的最大值
# - 也可以双指针做法，两个数组都排序后一次遍历
