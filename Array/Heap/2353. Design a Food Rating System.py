"""
LeetCode #2353 - Design a Food Rating System
设计食物评分系统
https://leetcode.cn/problems/design-a-food-rating-system/

设计一个支持下述操作的食物评分系统：
修改 系统中列出的某种食物的评分。
返回系统中某一类烹饪方式下评分最高的食物。
实现 `FoodRatings` 类：
`FoodRatings(String[] foods, String[] cuisines, int[] ratings)` 初始化系统。食物由 `foods`、`cuisines` 和 `ratings` 描述，长度均为 `n` 。
`foods[i]` 是第 `i` 种食物的名字。
`cuisines[i]` 是第 `i` 种食物的烹饪方式。
`ratings[i]` 是第 `i` 种食物的最初评分。
`void changeRating(String food, int newRating)` 修改名字为 `food` 的食物的评分。
`String highestRated(String cuisine)` 返回指定烹饪方式 `cuisine` 下评分最高的食物的名字。如果存在并列，返回 字典序较小 的名字。
注意，字符串 `x` 的字典序比字符串 `y` 更小的前提是：`x` 在字典中出现的位置在 `y` 之前，也就是说，要么 `x` 是 `y` 的前缀，或者在满足 `x[i] != y[i]` 的第一个位置 `i` 处，`x[i]` 在字母表中出现的位置在 `y[i]` 之前。

示例：
输入 ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"] [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]] 输出 [null, "kimchi", "ramen", null, "sushi", null, "ramen"]  解释 FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]); foodRatings.highestRated("korean"); // 返回 "kimchi"                                     // "kimchi" 是分数最高的韩式料理，评分为 9 。 foodRatings.highestRated("japanese"); // 返回 "ramen"                                       // "ramen" 是分数最高的日式料理，评分为 14 。 foodRatings.changeRating("sushi", 16); // "sushi" 现在评分变更为 16 。 foodRatings.highestRated("japanese"); // 返回 "sushi"                                       // "sushi" 是分数最高的日式料理，评分为 16 。 foodRatings.changeRating("ramen", 16); // "ramen" 现在评分变更为 16 。 foodRatings.highestRated("japanese"); // 返回 "ramen"                                       // "sushi" 和 "ramen" 的评分都是 16 。                                       // 但是，"ramen" 的字典序比 "sushi" 更小。

提示：
`1 <= n <= 2 * 10^4`
`n == foods.length == cuisines.length == ratings.length`
`1 <= foods[i].length, cuisines[i].length <= 10`
`foods[i]`、`cuisines[i]` 由小写英文字母组成
`1 <= ratings[i] <= 10^8`
`foods` 中的所有字符串 互不相同
在对 `changeRating` 的所有调用中，`food` 是系统中食物的名字。
在对 `highestRated` 的所有调用中，`cuisine` 是系统中 至少一种 食物的烹饪方式。
最多调用 `changeRating` 和 `highestRated` 总计 `2 * 10^4` 次
"""

from typing import List, Optional


import heapq
from collections import defaultdict


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine: dict = {}
        self.food_to_rating: dict = {}
        self.cuisine_to_heap: dict = defaultdict(list)  # stores (-rating, food)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            neg_rating, food = heap[0]
            # Check if the heap top has the current (non-outdated) rating
            if self.food_to_rating[food] == -neg_rating:
                return food
            heapq.heappop(heap)
        return ""



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Array, Hash Table, String, Ordered Set, Heap (Priority Queue)
#
# 解题思路:
# 使用三个数据结构：
# 1. food_to_cuisine: 记录每种食物所属的烹饪方式。
# 2. food_to_rating: 记录每种食物的当前评分（用于验证堆顶是否过期）。
# 3. cuisine_to_heap: 为每种烹饪方式维护一个大顶堆（用 -rating 模拟），
#    堆元素为 (-rating, food)，按评分降序、字典序升序排列。
# changeRating: 更新 food_to_rating 并将新 (-newRating, food) 推入对应 cuisine 的堆。
# highestRated: 不断弹出堆顶，直到堆顶的评分与 food_to_rating 中的一致（即未过期），返回食物名。
#
# 时间复杂度: changeRating O(log N), highestRated 均摊 O(log N)
# 空间复杂度: O(N) 其中 N 为食物数量
#
# 关键点:
# - 懒删除：评分更新时只推入新值，旧值在查询时被跳过
# - 堆元素为 (-rating, food)，Python 默认按元组字典序比较，可同时处理评分和名字排序
# - food_to_rating 作为权威数据源验证堆顶有效性
