"""
LeetCode #2285 - Maximum Total Importance of Roads
道路的最大总重要性
https://leetcode.cn/problems/maximum-total-importance-of-roads/

给你一个整数 `n` ，表示一个国家里的城市数目。城市编号为 `0` 到 `n - 1` 。
给你一个二维整数数组 `roads` ，其中 `roads[i] = [a_i, b_i]` 表示城市 `a_i` 和 `b_i` 之间有一条 双向 道路。
你需要给每个城市安排一个从 `1` 到 `n` 之间的整数值，且每个值只能被使用 一次 。道路的 重要性 定义为这条道路连接的两座城市数值 之和 。
请你返回在最优安排下，所有道路重要性 之和 最大 为多少。

示例 1：

输入：n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]] 输出：43 解释：上图展示了国家图和每个城市被安排的值 [2,4,5,3,1] 。 - 道路 (0,1) 重要性为 2 + 4 = 6 。 - 道路 (1,2) 重要性为 4 + 5 = 9 。 - 道路 (2,3) 重要性为 5 + 3 = 8 。 - 道路 (0,2) 重要性为 2 + 5 = 7 。 - 道路 (1,3) 重要性为 4 + 3 = 7 。 - 道路 (2,4) 重要性为 5 + 1 = 6 。 所有道路重要性之和为 6 + 9 + 8 + 7 + 7 + 6 = 43 。 可以证明，重要性之和不可能超过 43 。
示例 2：

输入：n = 5, roads = [[0,3],[2,4],[1,3]] 输出：20 解释：上图展示了国家图和每个城市被安排的值 [4,3,2,5,1] 。 - 道路 (0,3) 重要性为 4 + 5 = 9 。 - 道路 (2,4) 重要性为 2 + 1 = 3 。 - 道路 (1,3) 重要性为 3 + 5 = 8 。 所有道路重要性之和为 9 + 3 + 8 = 20 。 可以证明，重要性之和不可能超过 20 。

提示：
`2 <= n <= 5 * 10^4`
`1 <= roads.length <= 5 * 10^4`
`roads[i].length == 2`
`0 <= a_i, b_i <= n - 1`
`a_i != b_i`
没有重复道路。
"""

from typing import List, Optional


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        """
        Assign values 1..n to cities to maximize the sum of (city_a + city_b)
        for all roads. The optimal strategy: give higher values to cities
        with higher degree (more connected roads).
        """
        # Count degree of each city
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        # Sort degrees ascending
        degree.sort()

        # Assign values 1..n to cities sorted by degree
        # City with smaller degree gets smaller value, larger degree gets larger value
        total = 0
        for i, d in enumerate(degree):
            total += d * (i + 1)  # i+1 is the assigned value for this city

        return total


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Graph, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 1. 每条道路的贡献 = 两端城市的值之和。因此每条道路会将两个端点的值各计入总重要性一次。
# 2. 这意味着每个城市的值会被计算的次数等于该城市的度数（连接的道路数）。
# 3. 总重要性 = sum(degree[i] * value[i])，其中 degree[i] 是城市 i 的度数。
# 4. 为最大化总和，应该让度数高的城市获得更大的值（1 到 n）。
# 5. 算法：统计每个城市的度数 -> 对度数排序 -> 度数与赋值的点积即为答案。
#
# 时间复杂度: O(N + E log N)，N 为城市数，E 为道路数。统计度数 O(E)，排序 O(N log N)
# 空间复杂度: O(N)，用于存储度数数组
#
# 关键点:
# - 贪心策略：度数越高的城市分配越大的值
# - 不需要实际分配值，只需按排序后的度数加权求和 (degree_sorted[i] * (i+1))
# - 每条道路对总重要性的贡献等于两个端点值之和，等价于每个城市值乘以其度数
