"""
LeetCode #447 - Number of Boomerangs
中文题名：回旋镖的数量
https://leetcode.com/problems/number-of-boomerangs/

Given n points in the plane that are all pairwise distinct, a "boomerang" is
a tuple of points `(i, j, k)` such that the distance between `i` and
`j` equals the distance between `i` and `k` (the order
of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and
coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

【中文翻译】
给定平面上 n 个两两不同的点，"回旋镖"是一组点 (i, j, k)，使得 i 和 j 的距离
等于 i 和 k 的距离（考虑元组顺序）。求回旋镖的数量。n <= 500，坐标在 [-10000, 10000]。

示例：
    输入：[[0,0],[1,0],[2,0]]
    输出：2
    解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0

        for i, p in enumerate(points):
            dist_count = defaultdict(int)

            for j, q in enumerate(points):
                if i == j:
                    continue
                # Use squared distance to avoid floating point
                dx = p[0] - q[0]
                dy = p[1] - q[1]
                dist = dx * dx + dy * dy
                dist_count[dist] += 1

            # For each distance with m points, number of boomerangs = m * (m - 1)
            for count in dist_count.values():
                total += count * (count - 1)

        return total


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 哈希表 + 排列组合。对于每个点 i 作为回旋镖的中心：
# 1. 计算它到其他所有点的距离，用哈希表统计每种距离出现的次数
# 2. 对于距离为 d 的 m 个点，从中选 2 个分别作为 j 和 k，有 P(m,2) = m*(m-1) 种排列
#    （因为 (i,j,k) 是有序元组，选择顺序不同算不同的回旋镖）
# 3. 累加所有中心点的回旋镖数量
#
# 使用欧几里得距离的平方来代替距离，避免浮点数精度问题。
#
# 示例 [[0,0],[1,0],[2,0]]：
#   以 [1,0] 为中心：到 [0,0] 距离 1，到 [2,0] 距离 1 → m=2 → 2*(2-1)=2
#
# 时间复杂度: O(N^2) — 每个点对计算一次距离
# 空间复杂度: O(N) — 哈希表存储到其他点的距离
#
# 关键点:
# - 固定中心点 i，找与 i 距离相等的点对 (j,k)
# - 使用距离平方避免浮点误差
# - 排列数 m*(m-1)（有序对，不是无序对 m*(m-1)/2）
