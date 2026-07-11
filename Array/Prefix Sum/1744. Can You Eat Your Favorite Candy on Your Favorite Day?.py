"""
LeetCode #1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
中文题名：你能在你最喜欢的那天吃到你最喜欢的糖果吗？
https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

You are given a (0-indexed) array of positive integers `candiesCount`
where `candiesCount[i]` represents the number of candies of
the `ith` type you have. You are also given a 2D array
`queries` where `queries[i] = [favoriteTypei,
favoriteDayi, dailyCapi]`.

You play a game with the following rules:

You start eating candies on day `0`.

You cannot eat any candy of type `i` unless
you have eaten all candies of type `i - 1`.

You must eat at least one candy per day until
you have eaten all the candies.

Construct a boolean array `answer` such that `answer.length ==
queries.length` and `answer[i]` is `true` if you can eat
a candy of type `favoriteTypei` on day
`favoriteDayi` without eating more than
`dailyCapi` candies on any day, and `false`
otherwise. Note that you can eat different types of candy on the same day, provided
that you follow rule 2.

Return the constructed array `answer`.

Example 1:

Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
Output: [true,false,true]
Explanation:
1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
2- You can eat at most 4 candies each day.
If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.

Example 2:

Input: candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
Output: [false,true,true,false,false]

Constraints:

`1 <= candiesCount.length <= 105`

`1 <= candiesCount[i] <= 105`

`1 <= queries.length <= 105`

`queries[i].length == 3`

`0 <= favoriteTypei < candiesCount.length`

`0 <= favoriteDayi <= 109`

`1 <= dailyCapi <= 109`

【中文翻译】
给定糖果类型数组 candiesCount，candiesCount[i] 表示第 i 种糖果的数量。
你需要按顺序吃完所有糖果（必须吃完第 i 种糖果才能开始吃第 i+1 种）。
每天至少吃一个糖果。给定 queries[i] = [favoriteType, favoriteDay, dailyCap]，
判断是否能在第 favoriteDay 天（从0开始）吃到 favoriteType 类型的糖果（每天最多吃 dailyCap 个）。
返回布尔数组答案。

示例 1：
输入: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
输出: [true,false,true]
"""

from typing import List, Optional


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        # 前缀和：prefix[i] = 前 i 种糖果的总数
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + candiesCount[i]

        ans = []
        for ftype, fday, cap in queries:
            # 在第 fday 天（之前有 fday+1 天），最少吃 (fday + 1) 个，最多吃 (fday + 1) * cap 个
            min_eat = fday + 1
            max_eat = (fday + 1) * cap
            # 吃到第 ftype 种糖果需要已经吃完前 ftype 种：
            # 需要吃到至少 prefix[ftype] + 1，至多 prefix[ftype + 1] 个
            need_min = prefix[ftype] + 1
            need_max = prefix[ftype + 1]
            # 判断区间是否相交
            ans.append(not (max_eat < need_min or min_eat > need_max))

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和 + 区间判断。
# prefix[i] = 前 i 种糖果的总数。
# 对于查询 [ftype, fday, cap]：
# - 第 fday 天已经过了 fday+1 天，最少吃 (fday+1) 个，最多吃 (fday+1)*cap 个
# - 要吃到第 ftype 种，必须位于区间 [prefix[ftype]+1, prefix[ftype+1]]
# - 两个区间有交集即可：min_eat <= need_max AND max_eat >= need_min
#
# 时间复杂度: O(N + Q) — 前缀和 O(N)，每个查询 O(1)
# 空间复杂度: O(N) — 前缀和数组
#
# 关键点:
# - 将能否吃到转化为区间交集判断
# - 天数从 0 开始，所以到第 fday 天一共过了 fday+1 天
# - 注意糖果必须按顺序吃，不能跳着吃
