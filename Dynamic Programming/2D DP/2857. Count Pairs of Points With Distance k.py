"""
LeetCode #2857 - Count Pairs of Points With Distance k
统计距离为 k 的点对
https://leetcode.cn/problems/count-pairs-of-points-with-distance-k/

给你一个 二维 整数数组 `coordinates` 和一个整数 `k` ，其中 `coordinates[i] = [x_i, y_i]` 是第 `i` 个点在二维平面里的坐标。
我们定义两个点 `(x_1, y_1)` 和 `(x_2, y_2)` 的 距离 为 `(x1 XOR x2) + (y1 XOR y2)` ，`XOR` 指的是按位异或运算。
请你返回满足 `i < j` 且点 `i` 和点 `j`之间距离为 `k` 的点对数目。

示例 1：
输入：coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5 输出：2 解释：以下点对距离为 k ： - (0, 1)：(1 XOR 4) + (2 XOR 2) = 5 。 - (2, 3)：(1 XOR 5) + (3 XOR 2) = 5 。
示例 2：
输入：coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0 输出：10 解释：任何两个点之间的距离都为 0 ，所以总共有 10 组点对。

提示：
`2 <= coordinates.length <= 50000`
`0 <= x_i, y_i <= 10^6`
`0 <= k <= 100`
"""

from typing import List, Optional


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        ans = 0
        for x, y in coordinates:
            # Try all possible a values where a = x XOR x2
            for a in range(k + 1):
                b = k - a
                x2 = x ^ a
                y2 = y ^ b
                ans += freq.get((x2, y2), 0)
            freq[(x, y)] += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Hash Table
#
# 解题思路:
# 设 a = x1 XOR x2, b = y1 XOR y2，则 a + b = k。由于 k <= 100，可以枚举 a 从 0 到 k。
# 对于每个点 (x, y)，遍历每个可能的 a，计算目标坐标 (x XOR a, y XOR (k-a))，用哈希表统计已出现的相同坐标数量。
# 注意 i < j 的顺序，遍历时先查询哈希表再插入当前点，确保不会重复计算。
#
# 时间复杂度: O(n * k)
# 空间复杂度: O(n)
#
# 关键点:
# - 利用 k <= 100 的约束，枚举所有可能的 XOR 分量组合
# - x2 = x XOR a, y2 = y XOR (k-a)，直接在哈希表中查找
# - 先查后插，保证每个点对只被统计一次（i < j）
