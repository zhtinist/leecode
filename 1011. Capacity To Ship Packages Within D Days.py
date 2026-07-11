"""
LeetCode #1011 - Capacity To Ship Packages Within D Days
中文题名：在D天内送达包裹的能力
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

A conveyor belt has packages that must be shipped from one port to another within
`D` days.

The `i`-th package on the conveyor belt has a weight of `weights[i]`.
Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`).
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the
conveyor belt being shipped within `D` days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation:
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Note:

`1 <= D <= weights.length <= 50000`

`1 <= weights[i] <= 500`

【中文翻译】
传送带上有包裹必须在 `D` 天内从一个港口运送到另一个港口。

传送带上的第 `i` 个包裹的重量为 `weights[i]`。每一天，我们都会按 `weights` 给出的顺序将传送带上的包裹装载到船上。我们装载的重量不能超过船的最大运载重量。

返回能在 `D` 天内将传送带上所有包裹送达的船的最低运载能力。

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船只最低运载能力 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按给定顺序运输，因此使用运载能力为 14 的船只并将包裹分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。

示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船只最低运载能力 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

示例 3：

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1

注意：

`1 <= D <= weights.length <= 50000`

`1 <= weights[i] <= 500`

"""

from typing import List, Optional


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def can_ship(capacity: int) -> bool:
            days = 1
            total = 0
            for w in weights:
                if total + w > capacity:
                    days += 1
                    total = 0
                total += w
            return days <= D

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用二分搜索在可能的运载能力范围内查找最小值。
# 运载能力的下界为 max(weights)（至少能装下最重的包裹），上界为 sum(weights)（一天运完）。
# 对于每个中间值 mid，调用 can_ship(mid) 检查是否能在 D 天内运完：
# - 模拟每天装载，当累计重量超过 capacity 时，开启新的一天。
# - 如果所需天数 <= D，说明 capacity 可行。
# 如果可行则收缩右边界 right = mid，否则收缩左边界 left = mid + 1。
# 最终 left == right 即为最小可行运载能力。
#
# 时间复杂度: O(n * log(sum(weights))) - 二分搜索 log(sum) 次，每次 O(n) 模拟
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 下界为 max(weights)：船至少要能装下最重的单个包裹
# - 可以贪心装载：每天尽可能多地按顺序装包裹，不需要考虑拆分
# - 二分搜索的模板：可行时 right = mid，不可行时 left = mid + 1
