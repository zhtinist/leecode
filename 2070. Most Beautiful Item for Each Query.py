"""
LeetCode #2070 - Most Beautiful Item for Each Query
每一个查询的最大美丽值
https://leetcode.cn/problems/most-beautiful-item-for-each-query/

给你一个二维整数数组 `items` ，其中 `items[i] = [price_i, beauty_i]` 分别表示每一个物品的 价格 和 美丽值 。
同时给你一个下标从 0 开始的整数数组 `queries` 。对于每个查询 `queries[j]` ，你想求出价格小于等于 `queries[j]` 的物品中，最大的美丽值 是多少。如果不存在符合条件的物品，那么查询的结果为 `0` 。
请你返回一个长度与 `queries` 相同的数组 `answer`，其中 `answer[j]`是第 `j` 个查询的答案。

示例 1：
输入：items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6] 输出：[2,4,5,5,6,6] 解释： - queries[0]=1 ，[1,2] 是唯一价格 <= 1 的物品。所以这个查询的答案为 2 。 - queries[1]=2 ，符合条件的物品有 [1,2] 和 [2,4] 。   它们中的最大美丽值为 4 。 - queries[2]=3 和 queries[3]=4 ，符合条件的物品都为 [1,2] ，[3,2] ，[2,4] 和 [3,5] 。   它们中的最大美丽值为 5 。 - queries[4]=5 和 queries[5]=6 ，所有物品都符合条件。   所以，答案为所有物品中的最大美丽值，为 6 。
示例 2：
输入：items = [[1,2],[1,2],[1,3],[1,4]], queries = [1] 输出：[4] 解释： 每个物品的价格均为 1 ，所以我们选择最大美丽值 4 。 注意，多个物品可能有相同的价格和美丽值。
示例 3：
输入：items = [[10,1000]], queries = [5] 输出：[0] 解释： 没有物品的价格小于等于 5 ，所以没有物品可以选择。 因此，查询的结果为 0 。

提示：
`1 <= items.length, queries.length <= 10^5`
`items[i].length == 2`
`1 <= price_i, beauty_i, queries[j] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price
        items.sort(key=lambda x: x[0])

        # Precompute running maximum beauty
        n = len(items)
        prices = []
        max_beauty = []
        cur_max = 0
        for price, beauty in items:
            cur_max = max(cur_max, beauty)
            prices.append(price)
            max_beauty.append(cur_max)

        # Answer each query using binary search
        result = []
        for q in queries:
            # Find rightmost item with price <= q
            import bisect
            idx = bisect.bisect_right(prices, q) - 1
            if idx >= 0:
                result.append(max_beauty[idx])
            else:
                result.append(0)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Sorting
#
# 解题思路:
# 将items按价格排序。预计算价格递增序列中的运行最大美丽值。
# 对于每个查询q，使用二分查找找到最后一个价格<=q的物品的索引，
# 返回对应的最大美丽值。如果不存在则返回0。
#
# 时间复杂度: O((n + m) log n) 其中n=items数量, m=queries数量
# 空间复杂度: O(n)
#
# 关键点:
# - 按价格排序
# - 运行最大值（前缀最大值）
# - 二分搜索bisect_right
