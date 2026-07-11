"""
LeetCode #1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
中文题名：餐厅过滤器
https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

Given the array `restaurants` where  `restaurants[i] = [idi,
ratingi, veganFriendlyi, pricei, distancei]`.
You have to filter the restaurants using three filters.

The `veganFriendly` filter will be either true (meaning you
should only include restaurants with `veganFriendlyi` set to
true) or false (meaning you can include any restaurant). In
addition, you have the filters `maxPrice` and
`maxDistance` which are the maximum value for price and
distance of restaurants you should consider respectively.

Return the array of restaurant IDs after filtering, ordered
by rating from highest to lowest. For restaurants with the same
rating, order them by id from highest to lowest. For
simplicity `veganFriendlyi` and `veganFriendly`
take value 1 when it is true, and 0 when it is
false.

Example 1:

Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
Output: [3,1,5]
Explanation:
The restaurants are:
Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1]
After filter restaurants with veganFriendly = 1, maxPrice = 50 and maxDistance = 10 we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from highest to lowest).

Example 2:

Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
Output: [4,3,2,1,5]
Explanation: The restaurants are the same as in example 1, but in this case the filter veganFriendly = 0, therefore all restaurants are considered.

Example 3:

Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
Output: [4,5]

Constraints:

`1 <= restaurants.length <= 10^4`

`restaurants[i].length == 5`

`1 <= idi, ratingi, pricei,
distancei <= 10^5`

`1 <= maxPrice, maxDistance <= 10^5`

`veganFriendlyi` and `veganFriendly` are 0
or 1.

All `idi` are distinct.

【中文翻译】
给定一个餐厅数组 `restaurants`，其中 `restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]`。
你需要使用三个过滤器来筛选餐厅。

`veganFriendly` 过滤器为 true（表示只包含 `veganFriendlyi` 为 1 的餐厅）或
false（表示可以包含任何餐厅）。此外，还有 `maxPrice` 和 `maxDistance` 过滤器，
它们分别是你应考虑的餐厅价格和距离的最大值。

返回筛选后的餐厅 ID 数组，按评分从高到低排序。对于评分相同的餐厅，按 ID 从高到低排序。
为简化起见，`veganFriendlyi` 和 `veganFriendly` 在 true 时取值为 1，在 false 时取值为 0。

示例 1：

输入: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
输出: [3,1,5]
解释：
餐厅信息如下：
餐厅 1 [id=1, 评分=4, 素食友好=1, 价格=40, 距离=10]
餐厅 2 [id=2, 评分=8, 素食友好=0, 价格=50, 距离=5]
餐厅 3 [id=3, 评分=8, 素食友好=1, 价格=30, 距离=4]
餐厅 4 [id=4, 评分=10, 素食友好=0, 价格=10, 距离=3]
餐厅 5 [id=5, 评分=1, 素食友好=1, 价格=15, 距离=1]
使用 veganFriendly=1、maxPrice=50、maxDistance=10 筛选后，得到餐厅 3、餐厅 1 和餐厅 5（按评分从高到低排序）。

示例 2：

输入: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
输出: [4,3,2,1,5]
解释: 餐厅与示例 1 相同，但此时 veganFriendly=0，因此考虑所有餐厅。

示例 3：

输入: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
输出: [4,5]

约束条件：

`1 <= restaurants.length <= 10^4`

`restaurants[i].length == 5`

`1 <= idi, ratingi, pricei, distancei <= 10^5`

`1 <= maxPrice, maxDistance <= 10^5`

`veganFriendlyi` 和 `veganFriendly` 的取值为 0 或 1。

所有 `idi` 均不相同。
"""

from typing import List, Optional


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int
    ) -> List[int]:
        filtered = []
        for id_, rating, vegan, price, distance in restaurants:
            # 素食过滤器：只有 veganFriendly=1 时才需要 vegan=1
            if veganFriendly == 1 and vegan == 0:
                continue
            # 价格和距离过滤器
            if price > maxPrice or distance > maxDistance:
                continue
            filtered.append((rating, id_))

        # 按评分降序，评分相同按 ID 降序
        filtered.sort(key=lambda x: (x[0], x[1]), reverse=True)

        return [id_ for _, id_ in filtered]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 遍历餐厅数组，根据三个条件进行过滤：
#    - 素食友好过滤：仅当 veganFriendly=1 时才要求餐厅的 vegan 也为 1
#    - 价格过滤：price 不能超过 maxPrice
#    - 距离过滤：distance 不能超过 maxDistance
# 2. 将通过筛选的餐厅的 (评分, ID) 元组收集到列表中。
# 3. 对列表进行排序：优先按评分降序，评分相同按 ID 降序。
# 4. 返回排序后的 ID 列表。
#
# 时间复杂度: O(N log N) — 主要开销在排序，N 为餐厅数量
# 空间复杂度: O(N) — 存储筛选后的餐厅信息
#
# 关键点:
# - 素食过滤的条件逻辑：veganFriendly=0 时不需要检查 vegan 字段
# - 排序时使用双关键字：(评分降序, ID降序)
# - 可以直接在列表推导式中完成筛选和转换










